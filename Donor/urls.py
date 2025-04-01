from django.contrib import admin
from django.urls import path

from Donor import views

app_name="Donor"

urlpatterns = [
    path('Myprofile/',views.myprofile,name="myprofile"),
    path('EditProfile/',views.editprofile,name="editprofile"),
    path('ChangePassword/',views.changepassword,name="changepassword"),
    path('DonationHistory/',views.donationhistory,name="donationhistory"),


    path('CampDetails/',views.campdetails,name="campdetails"),

    path('complaintnew/',views.complaintnew,name="complaintnew"),
    path('Logout/',views.logout,name="logout"),



    path('donor_request/',views.donor_request,name="donor_request"),
    path('acceptrequest/<int:id>',views.acceptrequest,name="acceptrequest"),
    path('myaccepted/',views.myaccepted,name="myaccepted"),







    



]
