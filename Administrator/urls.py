from django.contrib import admin
from django.urls import path

from Administrator import views

app_name="Administrator"

urlpatterns = [

    path('AdminRegistration/',views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdmin/<int:delID>',views.delAdmin,name="delAdmin"),
    path('editAdminReg/<int:editID>',views.editAdminReg,name="editAdminReg"),

    path('ComplaintType/',views.ComplaintTypeInsertSelect,name="ComplaintTypeInsertSelect"),
    path('delcomplainttype/<int:delID>',views.delcomplainttype,name="delcomplainttype"),
    path('editcomplainttype/<int:editID>',views.editcomplainttype,name="editcomplainttype"),

    path('District/',views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:delID>',views.delDistrict,name="delDistrict"),
    path('editDistrict/<int:editID>',views.editDistrict,name="editDistrict"),

    path('Bloodgroup/',views.bloodgroupInsertSelect,name="bloodgroupInsertSelect"),
    path('delBlood/<int:delID>',views.delBlood,name="delBlood"),
    path('editBlood/<int:editID>',views.editBlood,name="editBlood"),

    path('Place/',views.placeInsertSelect,name="placeInsertSelect"),
    path('delplace/<int:delID>',views.delplace,name="delplace"),
    path('editplace/<int:editID>',views.editplace,name="editplace"),

    path('Notification/',views.notificationInsertSelect,name="notificationInsertSelect"),

    path('notifiiew/',views.notifiiew,name="notifiiew"),



    path('complaintView/',views.complaintView,name="complaintView"),

    path('Bloodbank/',views.BloodbankInsertSelect,name="BloodbankInsertSelect"),
    path('delBloodbank/<int:delID>',views.delBloodbank,name="delBloodbank"),
    path('editBloodbank/<int:editID>',views.editBloodbank,name="editBloodbank"),


    path('Logout/',views.logout,name="logout"),


    path('DonorVerification/',views.DonorVerificationInsert,name="DonorVerificationInsert"),

    path('PatientVerification/',views.PatientVerificationInsert,name="PatientVerificationInsert"),
    path('HomePage/',views.homeinsert,name="homeinsert"),

    
    path('CampDetails/',views.campdetails,name="campdetails"),
    path('approve/<int:id>',views.approve,name="approve"),
    path('reject/<int:id>',views.reject,name="reject"),



    path('PatientRequestData/',views.patientRequestData,name="patientRequestData"),
    path('complaintView/',views.complaintView,name="complaintView"),











]
