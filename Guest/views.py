from django.shortcuts import render,redirect
from Guest.models import *
from Administrator.models import *
from Donor.models import *

# Create your views here.

#for the donor registration : 

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
        # return render(request,'Guest/DonorRegistration.html',{'data':data,'blooddata':blooddata})
        return redirect("Guest:login")

    else:
        return render(request,'Guest/DonorRegistration.html',{'data':data,'blooddata':blooddata})
    
def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})

# patient registrstion
def patientInsert(request):
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
        password=request.POST.get('txtpwd')
        #for the ddl bloodgroup :
        bloodgroup=tbl_bloodgroup.objects.get(id=request.POST.get('selBloodgroup'))
        
        place=tbl_place.objects.get(id=request.POST.get('selPlace'))

        tbl_patient.objects.create(place=place,bloodgroup=bloodgroup,patient_name=name,
                                 patient_contact=contact,patient_email=email,patient_password=password,
                                 patient_address=address,
                                 patient_photo=photo,patient_age=age)
        # return render(request,'Guest/PatientRegistration.html',{'data':data,'blooddata':blooddata})
        return redirect("Guest:login")

    else:
        return render(request,'Guest/PatientRegistration.html',{'data':data,'blooddata':blooddata})
    
def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})

#Login page registration

def login(request):
    if request.method=="POST":
        email=request.POST.get('txtemail')
        password=request.POST.get('txtpwd')
        donorcount=tbl_donor.objects.filter(donor_email=email,donor_password=password).count()
        patientcount=tbl_patient.objects.filter(patient_email=email,patient_password=password).count()
        bloodbankcount=tbl_bloodbank.objects.filter(bloodbank_email=email,bloodbank_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()

        if donorcount>0:
            donor=tbl_donor.objects.get(donor_email=email,donor_password=password)
            request.session['did']=donor.id
            return redirect("Donor:myprofile")
        
        elif patientcount>0:
            patient=tbl_patient.objects.get(patient_email=email,patient_password=password)
            request.session['pid']=patient.id
            return redirect("Patient:myprofile")
        

        elif bloodbankcount>0:
            bloodbank=tbl_bloodbank.objects.get(bloodbank_email=email,bloodbank_password=password)
            request.session['bid']=bloodbank.id
            return redirect("Bloodbankapp:homeinsert")
        
        elif admincount>0:
            admin=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admin.id
            return redirect("Administrator:homeinsert")

        
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Data"})
    else:
        return render(request,'Guest/Login.html')
    

def index(request):
    
    return render(request,'Guest/index.html')


#search``


def donorlist(request):
    data=tbl_blooddonate.objects.all()
    return render(request,"Guest/Search.html",{'donor':data})


def ajaxsearch(request):
    data=tbl_blooddonate.objects.filter(donor__bloodgroup__Bloodgroup_name__istartswith=request.GET.get("name"))
    return render(request,"Guest/AjaxSearch.html",{'donor':data})