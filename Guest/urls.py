from django.contrib import admin
from django.urls import path

from Guest import views

app_name="Guest"

urlpatterns = [
    path('DonorRegistration/',views.donorInsert,name="donorInsert"),
    path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('PatientRegistration/',views.patientInsert,name="patientInsert"),
    path('Login/',views.login,name="login"),
    path('',views.index,name="index"),


    path('donorlist/',views.donorlist,name="donorlist"),
    path('ajaxsearch/',views.ajaxsearch,name="ajaxsearch"),





]
