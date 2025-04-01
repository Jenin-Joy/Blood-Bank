from django.shortcuts import render,redirect
from Guest.models import *
from Donor.models import *
from Patient.models import *

# Create your views here.
def myprofile(request):
    patient=tbl_patient.objects.get(id=request.session['pid'])
    return render(request,"Patient/Myprofile.html",{'data':patient})

def editprofile(request):
    patient=tbl_patient.objects.get(id=request.session['pid'])
    if request.method == "POST":
        patient.patient_name=request.POST.get("txtname")
        patient.patient_email=request.POST.get("txtemail")
        patient.patient_contact=request.POST.get("txtphone")
        
        patient.save()
        return redirect("Patient:myprofile")
    else:
        return render(request,"Patient/EditProfile.html",{'data':patient})
    

def changepassword(request):
    patient=tbl_patient.objects.get(id=request.session['pid'])
    dbpassword=patient.patient_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_oldpassword")
        newpassword=request.POST.get("txt_newpassword")
        conformpassword=request.POST.get("txt_cpassword")
        if dbpassword == oldpassword:
            if newpassword == conformpassword:
                patient.patient_password=newpassword
                patient.save()
                return redirect("Patient:myprofile")
            else:
                return render(request,"Patient/ChangePassword.html",{'msg':"Password MisMatch "})
        else:
            return render(request,"Patient/ChangePassword.html",{'msg':"Password Incorect "})
    else:
        return render(request,"Patient/ChangePassword.html")

#patient ajax place
def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Patient/Ajaxplace.html',{'place':place})



# patient request:

def patient_request(request):
    data=tbl_district.objects.all()
    patient=tbl_patient.objects.get(id=request.session['pid'])


    blooddata=tbl_bloodgroup.objects.all()

    if request.method=="POST":
        fordate=request.POST.get('txtfordate')
        bloodgroup=request.POST.get('selBloodgroup')
        unit=request.POST.get('txtunit')
        loc=request.POST.get('txtloc')
        #for the ddl bloodgroup :
        bloodgroup=tbl_bloodgroup.objects.get(id=request.POST.get('selBloodgroup'))
        
        place=tbl_place.objects.get(id=request.POST.get('selPlace'))

        tbl_request.objects.create(place=place,bloodgroup=bloodgroup,
                                   request_fordate=fordate,
                                   request_quantitiy=unit,patient=patient,
                                   request_location=loc
                                   )
        return render(request,'Patient/Patientrequest.html',{'data':data,'blooddata':blooddata})
    else:
        return render(request,'Patient/Patientrequest.html',{'data':data,'blooddata':blooddata})
    

def myRequestHistory(request):
    bloodunit=tbl_request.objects.filter(patient=request.session['pid'])
    return render(request,'Patient/MyRequestHistory.html',{'bloodunit':bloodunit})


#send new complaint 

def complaintnew(request):


    if request.method == "POST":
        content = request.POST.get("txtconm")
        tbl_complaint.objects.create(complaint_content=content,patient=tbl_patient.objects.get(id=request.session['pid']))
        return redirect('Patient:complaintnew')  # Redirect to clear form data
    else:
        return render(request,'Patient/Complaint.html')
    # notificationdata = tbl_complaint.objects.all()
    # return render(request, 'Patient/complaintnew.html', {'data': notificationdata})


# logout 
def logout(request):
    del request.session["pid"]
    return redirect("Guest:index")