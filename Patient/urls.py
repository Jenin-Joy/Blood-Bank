from django.contrib import admin
from django.urls import path

from Patient import views

app_name="Patient"

urlpatterns = [
    path('Myprofile/',views.myprofile,name="myprofile"),
    path('EditProfile/',views.editprofile,name="editprofile"),
    path('ChangePassword/',views.changepassword,name="changepassword"),


    path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('Patientrequest/',views.patient_request,name="patient_request"),
    path('MyRequestHistory/',views.myRequestHistory,name="myRequestHistory"),


    path('complaintnew/',views.complaintnew,name="complaintnew"),
    path('Logout/',views.logout,name="logout"),



]
