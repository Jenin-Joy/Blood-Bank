from django.shortcuts import render,redirect,get_object_or_404

from django.contrib import messages
from Administrator.models import *
from Guest.models import *
from Donor.models import *
from Patient.models import *
from Bloodbankapp.models import *
from django.db.models import Sum
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
    
def logout(request):
    del request.session["bid"]
    return redirect("Guest:index")

def myprofile(request):
    bloodbank=tbl_bloodbank.objects.get(id=request.session['bid'])
    return render(request,"Bloodbankapp/Myprofile.html",{'data':bloodbank})


def editprofile(request):
    bloodbank = get_object_or_404(tbl_bloodbank, id=request.session['bid'])
    
    if request.method == "POST":
        bloodbank.bloodbank_name = request.POST.get("txtname")
        bloodbank.bloodbank_email = request.POST.get("txtemail")
        bloodbank.bloodbank_contact = request.POST.get("txtphone")
        bloodbank.bloodbank_address = request.POST.get("txtaddr")

        district_id = request.POST.get("txtdist")
        if district_id:
            try:
                district = tbl_district.objects.get(id=district_id)
                bloodbank.district = district
            except tbl_district.DoesNotExist:
                messages.error(request, "Invalid district selected.")
                return redirect("Bloodbankapp:editprofile")

        bloodbank.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("Bloodbankapp:myprofile")
    else:
        districts = tbl_district.objects.all()
        return render(request, "Bloodbankapp/EditProfile.html", {'data': bloodbank, 'districts': districts})

def changepassword(request):
    # Safely get the bloodbank object or return 404
    bloodbank = get_object_or_404(tbl_bloodbank, id=request.session['bid'])
    dbpassword = bloodbank.bloodbank_password
    
    if request.method == "POST":
        oldpassword = request.POST.get("txt_oldpassword")
        newpassword = request.POST.get("txt_newpassword")
        conformpassword = request.POST.get("txt_cpassword")

        # Validate old password
        if dbpassword != oldpassword:
            messages.error(request, "Old password is incorrect.")
            return redirect("Bloodbankapp:changepassword")

        # Validate new password and confirm password match
        if newpassword != conformpassword:
            messages.error(request, "New password and confirm password do not match.")
            return redirect("Bloodbankapp:changepassword")

        # Basic password validation (e.g., minimum length)
        if len(newpassword) < 6:
            messages.error(request, "New password must be at least 6 characters long.")
            return redirect("Bloodbankapp:changepassword")

        # Update the password
        bloodbank.bloodbank_password = newpassword
        bloodbank.save()
        messages.success(request, "Password updated successfully!")
        return redirect("Bloodbankapp:myprofile")
    
    return render(request, "Bloodbankapp/ChangePassword.html")

# donorList 
def donorlist(request):
    data=tbl_donor.objects.all()
    donatedata=tbl_blooddonate.objects.all()
    return render(request,"Bloodbankapp/Donorlist.html",{'donor':data,"donate":donatedata})


def ajaxsearch(request):
    data=tbl_donor.objects.filter(donor_name__istartswith=request.GET.get("name"))
    return render(request,"Bloodbankapp/AjaxSearch.html",{'donor':data})


#new Donor registration:


def donorInsert(request):
    data=tbl_district.objects.all()

    blooddata=tbl_bloodgroup.objects.all()

    if request.method=="POST":
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        age=request.POST.get('txtage')
        contact=request.POST.get('txtphone')
        address=request.POST.get('txtaddr')
        photo=request.FILES.get('filePhoto')
        bloodgroup=request.POST.get('selBloodgroup')
        disease=request.POST.get('txtdise')
        password=request.POST.get('txtpwd')
        #for the ddl bloodgroup :
        bloodgroup=tbl_bloodgroup.objects.get(id=request.POST.get('selBloodgroup'))
        
        place=tbl_place.objects.get(id=request.POST.get('selPlace'))

        tbl_donor.objects.create(place=place,bloodgroup=bloodgroup,donor_name=name,
                                 donor_contact=contact,donor_email=email,donor_password=password,donor_address=address,
                                 donor_photo=photo,disease_status=disease,donor_age=age)
        return render(request,'Bloodbankapp/DonorRegistration.html',{'data':data,'blooddata':blooddata})
    else:
        return render(request,'Bloodbankapp/DonorRegistration.html',{'data':data,'blooddata':blooddata})
    
def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Bloodbankapp/Ajaxplace.html',{'place':place})


def addDetails(request,id):
    data=tbl_blooddonate.objects.all()
    donor=tbl_donor.objects.get(id=id)
    # print(donor.bloodgroup.Bloodgroup_name)
    
    if request.method=="POST":
        unit=request.POST.get('txtunit')
        donor=tbl_donor.objects.get(id=id)
        tbl_blooddonate.objects.create(blooddonate_unit=unit,donor=donor,bloodbank=tbl_bloodbank.objects.get(id=request.session['bid']))

        return redirect('Bloodbankapp:donorlist')
    else:
        return render(request,'Bloodbankapp/AddDetails.html',{'data':data,'donor':donor})
    
    #Home 

def homeinsert(request):

    # bloodbank=tbl_bloodbank.objects.get(id=request.session['bid'])
    bloodcat = tbl_bloodgroup.objects.all()
    for i in bloodcat:
        count = tbl_blooddonate.objects.filter(bloodbank=request.session["bid"],donor__bloodgroup=i.id).aggregate(total=Sum("blooddonate_unit"))['total'] or 0
        req = tbl_request.objects.filter(bloodgroup=i.id,request_status=1).aggregate(total=Sum("request_quantitiy"))["total"] or 0
        total= count - req
        i.bloodcount = total

    return render(request,'Bloodbankapp/Home.html',{"blood":bloodcat})

# {'data':bloodbank}

# patient approval process 
def patientRequest(request):
    bloodunit=tbl_request.objects.all()
    for i in bloodunit:
        count = tbl_blooddonate.objects.filter(bloodbank=request.session["bid"],donor__bloodgroup=i.bloodgroup.id).aggregate(total=Sum("blooddonate_unit"))['total'] or 0
        req = tbl_request.objects.filter(bloodgroup=i.bloodgroup.id,request_status=1).aggregate(total=Sum("request_quantitiy"))["total"] or 0
        total= count - req
        i.bloodcount = int(total)
        i.unit  = int(i.request_quantitiy)
    return render(request,'Bloodbankapp/PatientRequest.html',{'bloodunit':bloodunit})

#approve buttom 

def approve(request, id):
    approve = tbl_request.objects.get(id=id)
    approve.request_status = 1
    approve.save()

    # Get the user's email (assuming there's a user associated with the request)
    email = approve.patient.patient_email    

    # Email content
    subject = "Blood Request Approved"
    message = (
        f"Hi {approve.patient.patient_name},\n\n"
        "Your request has been approved by the Blood Bank.\n\n"
        "For further information, please log in to your account on BloodHive.\n\n"
        "Contact:\n"
        f"📧 Email: {settings.EMAIL_HOST_USER}\n\n"
        "The blood will arrive at your location soon.\n\n"
        "Best regards,\n"
        "BloodHive Team"
    )

    # Send email
    send_mail(
        subject,  
        message,  
        settings.EMAIL_HOST_USER,  
        [email],  
    )

    return redirect("Bloodbankapp:patientRequest")



#donorrequest 


def req(request, id):
    approve = tbl_request.objects.get(id=id)
    bloodgroup=approve.bloodgroup

    approve.request_status = 3
    approve.save()
    reque = tbl_blooddonate.objects.filter(donor__bloodgroup=bloodgroup)
    for i in reque:
        email = i.donor.donor_email

        name = i.donor.donor_name   
        pname = approve.patient.patient_name

        pcon = approve.patient.patient_contact
        ploc = approve.request_location
        # Email content
        subject = "Blood Request Approved"
        message = (
            f"Hi {name},\n\n"
            f"There  is an urgent request for the blood by the patient : {pname} from the Blood Bank.\n\n"
            "For further information, please log in to your account on BloodHive.\n\n"
            "Patient Contact Details:\n"
            f"patient contact :{pcon}\n"
            f"patient location  :{ploc}\n"

            f"📧 Email: {settings.EMAIL_HOST_USER}\n\n"
            "This  blood will save the life of the others .\n\n"
            "Best regards,\n"
            "BloodHive Team"
        )

        # Send email
        send_mail(
            subject,  
            message,  
            settings.EMAIL_HOST_USER,  
            [email],  
        )

    return redirect("Bloodbankapp:patientRequest")

def reject(request,id):
    approve=tbl_request.objects.get(id=id)
    approve.request_status=2
    approve.save()
    return redirect("Bloodbankapp:patientRequest")

    






#complaint  view
def complaintView(request):
    complaint = tbl_complaint.objects.all()
    return render(request,'Bloodbankapp/ComplaintView.html',{'data':complaint})

# Camp

def campInsertSelect(request):
    # campdata=tbl_camp.objects.all()

    # blooddata=tbl_bloodgroup.objects.all()   
    bloodbank=tbl_bloodbank.objects.get(id=request.session['bid'])

    data=tbl_district.objects.all()

    if request.method=="POST":
        date=request.POST.get('txtdob')
        detail=request.POST.get('txtdetails')

        # detail=request.POST.get('txtdetails')

        # place=request.POST.get('selDistrict')

        place=tbl_place.objects.get(id=request.POST.get('selPlace'))

        tbl_camp.objects.create(camp_date=date,place=place,camp_details=detail,bloodbank=bloodbank)
        return render(request,'Bloodbankapp/Camp.html',{'data':data,'bloodbank':bloodbank})
    else:
        return render(request,'Bloodbankapp/Camp.html',{'data':data,'bloodbank':bloodbank})


#camp details 

def campdetails (request):
    data=tbl_camp.objects.all()
    return render(request,'Bloodbankapp/CampDetails.html',{'data':data})


#Notification

def notificationInsertSelect(request):
    if request.method == "POST":
        content = request.POST.get("txtcon")
        tbl_Notification.objects.create(notification_content=content)
        return redirect('Bloodbankapp:notificationInsertSelect')  # Redirect to clear form data

    notificationdata = tbl_Notification.objects.all()
    return render(request, 'Bloodbankapp/Notification.html', {'data': notificationdata})


#notifaction view

def notifiiew(request):

    notificationdata=tbl_Notification.objects.all()
    return render(request,'Bloodbankapp/NotificationView.html',{'data':notificationdata})




#search

def searchlist(request):
    data=tbl_blooddonate.objects.all()
    return render(request,"Bloodbankapp/Search.html",{'donor':data})



def ajaxsearchlist(request):
    data=tbl_blooddonate.objects.filter(donor__bloodgroup__Bloodgroup_name__istartswith=request.GET.get("name"))
    return render(request,"Bloodbankapp/AjaxSearchlist.html",{'donor':data})

# sendmail


# def sendrequest(request):

#     fin=tbl_request.objects.filter(bloodgroup=request)


#     dt=tbl_blooddonate.objects.all()














 