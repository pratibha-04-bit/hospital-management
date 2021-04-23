from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Department,Doctor,Doctor_details,Leave_form,Appointment
# from .models import Department,Doctor,Leave_form,Appointment
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth






def home1(request):
    return render(request,'home1.html')

def home3(request):
    return render(request,'home3.html')

@csrf_exempt
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("doctor")
        else:
            messages.info(request,'invalid credentials')
            return redirect("login")   
    else:
        return render(request,'login.html')  

def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # print("username taken")
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # print("email taken")  
                messages.info(request,'email taken')
                return redirect('register')  
            else:
                user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

                
        else:
            # print('password not matching ')
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')        
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home3')


# Department page
    
def dept(request):
    return render(request,'dept.html')

def create_dept(request):
    department = Department(
        deptno = request.POST['deptno'],
        dname = request.POST['dname']
    )
    department.save()
    return redirect('show_dept')

def show_dept(request):
    departments=Department.objects.all()
    context ={'departments':departments}
    return render(request,'dept.html',context)

# doctor page 

def doctor(request):
    results = Department.objects.all().values('dname','id')
    context = {'results':results}
    return render(request,'doctor.html',context)
    
def doctor_create(request):
    doctor=Doctor(
        doc_no = request.POST['doc_no'],
        doc_name = request.POST['doc_name'],
        doc_phone = request.POST['doc_phone'],
        doc_email = request.POST['doc_email'],
        department_id = request.POST['department_id'],
        doj = request.POST['doj'],
        gender = request.POST['gender'],
        # image = request.FILES['image_upload']
        )
    doctor.save()
    return redirect('./doctor_detail')

def doctor_detail(request):
    doctors=Doctor_details.objects.all()
    context = {'doctors':doctors}
    return render(request,'doctor_detail.html',context)
    
def doctor_model(request,id):
    doctor = Doctor_details.objects.filter(id=id)
    data = serializers.serialize('json',doctor)
    return HttpResponse(data,content_type="application/json")

def doctor_update(request):
    id=request.POST['id']
    doctor = Doctor.objects.get(id=id)
    doctor.doc_no = request.POST['doc_no']
    doctor.doc_name = request.POST['doc_name']
    doctor.doc_email = request.POST['doc_email']
    doctor.dept = request.POST['dept']
    doctor.doj = request.POST['doj']
    doctor.gender = request.POST['gender']
    doctor.save()
    return HttpResponse(True)

def delete(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return HttpResponse(True)

# search of doctor
def search(request):
    if request.method=="POST":
        srch = request.POST['srh']
        if srch:
            match = Doctor_details.objects.filter(Q(doc_no=srch)|
                                          Q(doc_name=srch)|
                                          Q(dname=srch)
                                          )
            if match:
                return render(request,'doctor_detail.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return render(request,'./doctor_detail')
    return render(request,'doctor_detail.html') 


def leave_form(request):
    departments = Department.objects.all().values('dname','id')
    context = {'departments':departments}
    return render(request,'leave_form.html',context)

def save_leave(request):
    leave = Leave_form(
        doctor_no = request.POST['doctor_no'],
        # available= request.POST['available'],
        doctor_name = request.POST['doctor'],
        department = request.POST['dept_list'],
        date = request.POST['date']
    )
    # doctor_name = request.POST['doctor_name']
    # if Doctor_details.objects.filter(doc_name=doctor_name).exists():
    #     print("name:" + request.POST['doctor_name'])
    # else:
    #     messages.info(request,'name not found')
    leave.save()
    return redirect('./check')


def check(request):
    leave = Leave_form.objects.all()
    context={'leave':leave}
    return render(request,'check.html',context)    

def leave_modal(request,id):
    leave_details = Leave_form.objects.filter(id=id)
    data = serializers.serialize('json', leave_details)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def check_update(request):
    id=request.POST['id']
    leave = Leave_form.objects.get(id=id)
    leave.doctor_no=request.POST['doctor_no']
    leave.doctor_name=request.POST['doctor_name']
    leave.department=request.POST['department']
    leave.date=request.POST['date']
    leave.status=request.POST['status']
    leave.save()
    return HttpResponse(True)

        

def appointment(request):
    departments=Department.objects.all()
    doctors = Doctor_details.objects.all()

    return render(request,'appointment.html',{'departments':departments,'doctors':doctors})


def get_doctors(request,id):
    doctors =  Doctor.objects.filter(department_id=id)
    data = serializers.serialize('json',doctors)
    return HttpResponse(data,content_type="application/json")

@csrf_exempt
def appointment_save(request):
    appoint_date=request.POST['appointment_date']
    appointment = Appointment(
        patient_name=request.POST['patient_name'],
        age = request.POST['age'],
        department = request.POST['department'],
        doctor=request.POST['doctor'],
        appointment_date=appoint_date,
        gender=request.POST['gender']
        
    )

    # result =Leave_form.objects.all().values('status')
    # print( result)
    if Leave_form.objects.filter(date=appoint_date):
        if Leave_form.objects.filter(status='Not available'):
            print('choose another')
            messages.info(request,'Doctor is not available ')
    else:
        print('done')
        appointment.save()
    return HttpResponse(True)


