from django.db import models
from datetime import datetime, date

class Registration(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=40)
    TYPE_CHOICES = [
        ('male', 'male'),
        ('female', 'female')
                   ]
    gender = models.CharField(max_length=10 ,choices=TYPE_CHOICES)

    class Meta:
        db_table = "registration"               


class Department(models.Model):
    deptno = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)

    class Meta:
        db_table = "department"

class Doctor(models.Model):
    doc_no = models.CharField(max_length=50)
    doc_name = models.CharField(max_length=70)
    doc_phone = models.IntegerField()
    doc_email = models.EmailField(max_length=50)
    department_id = models.IntegerField() 
    doj = models.DateField( auto_now = False)
    gender = models.CharField(max_length=20)
    # image = models.ImageField(upload_to= 'pics',default='')

    class Meta:
         db_table="doctor"

# view
class Doctor_details(models.Model):
    doc_no = models.CharField(max_length=50)
    doc_name = models.CharField(max_length=70)
    doc_phone = models.IntegerField()
    doc_email = models.EmailField(max_length=50)
    department_id = models.IntegerField() 
    dname = models.CharField(max_length=70)
    doj = models.DateField( auto_now = False)
    gender = models.CharField(max_length=20)

    class Meta:
        
         db_table="doctor_details"         

class Leave_form(models.Model):
    doctor_no = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=70)
    department = models.CharField(max_length=50)
    date = models.DateField( auto_now = False)
    TYPE_CHOICES = [
        ('available', 'available'),
        ('Not available', 'Not available')
                   ]
    status = models.CharField(max_length=20,default="Not Available",choices=TYPE_CHOICES)
    

    class Meta:
        db_table="leave_form"

class Appointment(models.Model):
    patient_name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    appointment_date = models.DateField(auto_now=False)
    gender = models.CharField(max_length=10)

    class Meta:
        db_table="appointment"

class Login(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    
    class Meta:
        db_table="login"