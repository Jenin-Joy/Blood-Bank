from django.contrib import admin
from django.urls import path

from Bloodbankapp import views

app_name="Bloodbankapp"

urlpatterns = [
    path('Myprofile/',views.myprofile,name="myprofile"),
    path('EditProfile/',views.editprofile,name="editprofile"),
    path('ChangePassword/',views.changepassword,name="changepassword"),
    path('donorlist/',views.donorlist,name="donorlist"),
    path('ajaxsearch/',views.ajaxsearch,name="ajaxsearch"),

    path('DonorRegistration/',views.donorInsert,name="donorInsert"),
    path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('AddDetails/<int:id>',views.addDetails,name="addDetails"),
    path('Home/',views.homeinsert,name="homeinsert"),
    path('PatientRequest/',views.patientRequest,name="patientRequest"),

    path('Logout/',views.logout,name="logout"),


    path('Camp/',views.campInsertSelect,name="campInsertSelect"),

    path('CampDetails/',views.campdetails,name="campdetails"),
    path('req/<int:id>',views.req,name="req"),


    path('approve/<int:id>',views.approve,name="approve"),
    path('reject/<int:id>',views.reject,name="reject"),

    

    path('Notification/',views.notificationInsertSelect,name="notificationInsertSelect"),

    path('notifiiew/',views.notifiiew,name="notifiiew"),
    path('complaintView/',views.complaintView,name="complaintView"),


    path('searchlist/',views.searchlist,name="searchlist"),

    path('ajaxsearchlist/',views.ajaxsearchlist,name="ajaxsearchlist"),

]
