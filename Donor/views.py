from django.shortcuts import render,redirect, get_object_or_404
from Guest.models import *
from Guest.models import *
from Bloodbankapp.models import *
from Donor.models import *
from Administrator.models import *
from Patient.models import *


# Create your views here.
def myprofile(request):
    donor=tbl_donor.objects.get(id=request.session['did'])
    return render(request,"Donor/Myprofile.html",{'data':donor})

def editprofile(request):
    donor=tbl_donor.objects.get(id=request.session['did'])
    if request.method == "POST":
        donor.donor_name=request.POST.get("txtname")
        donor.donor_email=request.POST.get("txtemail")
        donor.donor_contact=request.POST.get("txtphone")
        
        donor.save()
        return redirect("Donor:myprofile")
    else:
        return render(request,"Donor/EditProfile.html",{'data':donor})
    

def changepassword(request):
    donor=tbl_donor.objects.get(id=request.session['did'])
    dbpassword=donor.donor_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_oldpassword")
        newpassword=request.POST.get("txt_newpassword")
        conformpassword=request.POST.get("txt_cpassword")
        if dbpassword == oldpassword:
            if newpassword == conformpassword:
                donor.donor_password=newpassword
                donor.save()
                return redirect("Donor:myprofile")
            else:
                return render(request,"Donor/ChangePassword.html",{'msg':"Password MisMatch "})
        else:
            return render(request,"Donor/ChangePassword.html",{'msg':"Password Incorect "})
    else:
        return render(request,"Donor/ChangePassword.html")
    



#donation history

def donationhistory(request):
    bloodunit=tbl_blooddonate.objects.filter(donor=request.session['did'])
    return render(request,'Donor/DonationHistory.html',{'bloodunit':bloodunit})




#camp details 

def campdetails (request):
    data=tbl_camp.objects.all()
    return render(request,'Donor/CampDetails.html',{'data':data})
# complaint send 

def complaintnew(request):


    if request.method == "POST":
        content = request.POST.get("txtconm")
        tbl_complaint.objects.create(complaint_content=content,donor=tbl_donor.objects.get(id=request.session['did']))
        return redirect('Donor:complaintnew')  # Redirect to clear form data
    else:
        return render(request,'Donor/Complaint.html')
    

#logout 
def logout(request):
    del request.session["did"]
    return redirect("Guest:index")


#requst approvable 

# def requ(request):
#      # Get all requests with status = 3
#     matching_requests = tbl_request.objects.filter(request_status=3)

#     donor_notifications = []  # List to store donors who match the request
    
#     for blood_request in matching_requests:
#         # Find donors with the same bloodgroup
#         matching_donors = tbl_donor.objects.filter(bloodgroup=blood_request.bloodgroup)

#         for donor in matching_donors:
#             donor_notifications.append({
#                 "donor_name": donor.donor_name,
#                 "donor_email": donor.donor_email,
#                 "bloodgroup": donor.bloodgroup.Bloodgroup_name,
#                 "request_id": blood_request.id,
#                 "request_quantity": blood_request.request_quantitiy,
#                 "request_location": blood_request.request_location,
#             })

#     return render(request, "Donor/Request.html", {"notifications": donor_notifications})





# def req(request, id):
#     approve = tbl_request.objects.get(id=id)
#     bloodgroup=approve.bloodgroup
#     reque = tbl_blooddonate.objects.filter(donor__bloodgroup=bloodgroup,request_status=3)
#     return render(request, "Donor/Request.html", {"notifications": reque,"approve":approve})



# def req(request, id):
#     approve = get_object_or_404(tbl_request, id=id)  # Get the request or return 404
#     bloodgroup = approve.bloodgroup  # Get blood group of the request

#     # Find matching blood donations
#     reque = tbl_blooddonate.objects.filter(donor__bloodgroup=bloodgroup)

#     return render(request, "Donor/Request.html", {"notifications": reque, "approve": [approve]}) 




# def reque(request, id):
#     # Get the specific request
#     approve = get_object_or_404(tbl_request, id=id, request_status=3)  

#     # Get donors with the same blood group
#     matching_donors = tbl_donor.objects.filter(bloodgroup=approve.bloodgroup)

#     return render(request, "Donor/Request.html", {
#         "approve": approve,  # Single request
#         "notifications": matching_donors  # List of matching donors
#     })


#


def donor_request(request):
    donor = tbl_donor.objects.get(id=request.session["did"])
    req = tbl_request.objects.filter(request_status=3,bloodgroup=donor.bloodgroup.id,place=donor.place.id)
    return render(request, "Donor/Request.html",{"blood_requests":req})

def acceptrequest(request, id):
    req = tbl_request.objects.get(id=id)
    req.request_status = 4
    req.donor = tbl_donor.objects.get(id=request.session["did"])
    req.save()
    return render(request, "Donor/Request.html",{"msg":"You accepted the request"})

def myaccepted(request):
    req = tbl_request.objects.filter(donor=request.session["did"],request_status=4)
    return render(request,"Donor/AcceptedRequest.html",{"request":req})