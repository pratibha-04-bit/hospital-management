from django.urls import path
from . import views

urlpatterns=[
  
  
    path('home1',views.home1,name="home1"),
     path('home3',views.home3,name="home3"),
    # path('home2',views.home2,name="home2"),
    path('login',views.login,name='login'),
   
    path("logout",views.logout, name = "logout"),

    #registration
    path('register',views.register,name="register"),

    # department
    path('dept',views.dept,name="dept"),
    path('create_dept',views.create_dept,name="create_dept"),
    path('show_dept',views.show_dept,name="show_dept"),
    
    # doctor
    path('doctor',views.doctor,name="doctor"),
    path('doctor_create',views.doctor_create,name="doctor_create"),
    path('doctor_detail',views.doctor_detail,name="doctor_detail"),
    path('doctor_modal/<int:id>',views.doctor_model,name="doctor_modal"),
    path('doctor_update',views.doctor_update,name="doctor_update"),
    path('delete/<int:id>',views.delete,name='delete'),

    #search
    path('search',views.search,name="search"),

    #doctor avaibility
    path('leave_form',views.leave_form,name="leave_form"),
    path('save_leave',views.save_leave,name="save_leave"),
    path('check',views.check,name="check"),
    path('leave_modal/<int:id>',views.leave_modal,name="leave_modal"),
    path('check_update',views.check_update,name="check_update"),
    path('get_doctors/<int:id>',views.get_doctors,name="get_doctors"),

    # appointment
    path('appointment',views.appointment,name="appointment"),
    path('appointment_save',views.appointment_save,name="appointment_save")

]