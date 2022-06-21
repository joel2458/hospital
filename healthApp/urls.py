from django.contrib import admin
from django.urls import path,include
from.import views


urlpatterns = [
           path('',views.homepage,name='homepage'),
    path('adminhome',views.adminhome,name='adminhome'),

    path('doctorsignup',views.doctorsignup,name='doctorsignup'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('user_login',views.user_login,name='user_login'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('logout',views.logout,name='logout'),

    path('load_add_department',views.load_add_department,name='load_add_department'),
    path('add_department',views.add_department,name='add_department'),
    path('show_doctor',views.show_doctor,name='show_doctor'),
    # path('load_doctor_details/<int:pk>',views.load_doctor_details,name='load_doctor_details'),
    path('add_doctor_details/<int:pk>',views.add_doctor_details,name='add_doctor_details'),
    path('showdoc/<int:pk>',views.showdoc,name='showdoc'),
    # path('docdep',views.docdep,name='docdep'),
    path('show_dep',views.show_dep,name='show_dep'),
    path('detail/<int:pk>',views.detail,name='detail'),
    # path('user_showdoctor',views.user_showdoctor,name='user_showdoctor'),
    # path('show_d',views.show_d,name='show_d'),

    # path('homedep',views.homedep,name='homedep'),

    path('delete_doctor/<int:pk>',views.delete_doctor,name='delete_doctor'),
    # path('showdepdoc/<int:pk>',views.showdepdoc,name='showdepdoc'),



    path('load_doctor_home',views.load_doctor_home,name='load_doctor_home'),
    path('doctor_profile/<int:pk>',views.doctor_profile,name='doctor_profile'),
    # path('doctor_dep/<int:pk>',views.doctor_dep,name='doctor_dep')
    path('user_edit_profile',views.user_edit_profile,name='user_edit_profile'),


    # path('load_patient_signup',views.load_patient_signup,name='load_patient_signup'),
    # path('patient_signup',views.patient_signup,name='patient_signup'),
    # path('patient_login',views.patient_login,name='patient_login'),
    # path('patientlogin',views.patientlogin,name='patientlogin'),
    # path('patienthome',views.patienthome,name='patienthome'),

    # path('load_appoinment',views.load_appoinment,name='load_appoinment'),
    path('appoinments',views.appoinments,name='appoinments'),

    # path('show_appoinment/<int:pk>',views.show_appoinment,name='show_appoinment'),
    path('sndmail/<int:pk>',views.sndmail,name='sndmail'),


]