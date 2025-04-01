from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from Bloodbankapp.models import *
from Patient.models import *
from Donor.models import *
from django.db.models import Sum




# Create your views here.
#This Section AdminRegistration Opertions
def adminInsertSelect(request):
    admindata=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        contact=request.POST.get('txtphone')
        password=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=password)
        return render(request,'Administrator/AdminRegistration.html',{'data':admindata})
    else:
        return render(request,'Administrator/AdminRegistration.html',{'data':admindata})


def delAdmin(request,delID):
    tbl_admin.objects.get(id=delID).delete()
    return redirect("Administrator:adminInsertSelect")
    
def editAdminReg(request,editID):
    ed=tbl_admin.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        contact=request.POST.get('txtphone')
        password=request.POST.get('txtpwd')
        ed.admin_name=name
        ed.admin_contact=contact
        ed.admin_email=email
        ed.admin_password=password
        ed.save()
        """save() is the savefunction in django """
        return redirect("Administrator:adminInsertSelect")
    else:
        return render(request,"Administrator/AdminRegistration.html",{'edit':ed})

#District section 
#start from this :
def districtInsertSelect(request):
    districtData = tbl_district.objects.all()
    if request.method=="POST":
        districtName = request.POST.get('txtdist')
        tbl_district.objects.create(district_name = districtName)
        return render(request,'Administrator/District.html',{'districtData':districtData})
    else:
        return render(request,'Administrator/District.html',{'districtData':districtData})

def delDistrict(request,delID):
    tbl_district.objects.get(id=delID).delete()
    return redirect("Administrator:districtInsertSelect")

def editDistrict(request,editID):
    ed=tbl_district.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtdist")
        ed.district_name=name
        ed.save()
        """save() is the savefunction in django """
        return redirect("Administrator:districtInsertSelect")
    else:
        return render(request,"Administrator/District.html",{'edit':ed})
    
    
#Complaint section start from this :    
def ComplaintTypeInsertSelect(request):
    ComplaintTypedata = tbl_complainttype.objects.all()
    if request.method=="POST":
        Complainttypename = request.POST.get('txtname')
        tbl_complainttype.objects.create(complainttype_name = Complainttypename)
        return render(request,'Administrator/ComplaintType.html',{'ComplaintTypedata':ComplaintTypedata})
    else:
        return render(request,'Administrator/ComplaintType.html',{'ComplaintTypedata':ComplaintTypedata})
    



#complaint  view
def complaintView(request):
    complaint = tbl_complaint.objects.all()
    return render(request,'Administrator/ComplaintView.html',{'data':complaint})




    
def delcomplainttype(request,delID):
    tbl_complainttype.objects.get(id=delID).delete()
    return redirect("Administrator:ComplaintTypeInsertSelect")

def editcomplainttype(request,editID):
    ed=tbl_complainttype.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtname")
        ed.complainttype_name=name
        ed.save()
        """save() is the savefunction in django """
        return redirect("Administrator:ComplaintTypeInsertSelect")
    else:
        return render(request,"Administrator/ComplaintType.html",{'edit':ed})
    

#Bloodgroup section start from this :
   
def bloodgroupInsertSelect(request):
    blooddata=tbl_bloodgroup.objects.all()
    if request.method=="POST":
        bloodname = request.POST.get('txtname')
        tbl_bloodgroup.objects.create(Bloodgroup_name = bloodname)
        return render(request,'Administrator/Bloodgroup.html',{'blooddata':blooddata})
    else:
        return render(request,'Administrator/Bloodgroup.html',{'blooddata':blooddata})

def delBlood(request,delID):
    tbl_bloodgroup.objects.get(id=delID).delete()
    return redirect("Administrator:bloodgroupInsertSelect")
 
def editBlood(request,editID):
    ed=tbl_bloodgroup.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtname")
        ed.Bloodgroup_name=name
        ed.save()
        return redirect("Administrator:bloodgroupInsertSelect")
    else:
        return render(request,"Administrator/Bloodgroup.html",{'edit':ed})
    


#Place sectiion start from this :
def placeInsertSelect(request):
    placeData=tbl_place.objects.all()
    districtData=tbl_district.objects.all()
    if request.method=="POST":
        placename = request.POST.get('txtplace')
        district=tbl_district.objects.get(id=request.POST.get('selDistrict'))
        tbl_place.objects.create(place_name=placename,district=district)
        return render(request,'Administrator/Place.html',{'placeData':placeData,'districtData':districtData})
    else:
        return render(request,'Administrator/Place.html',{'placeData':placeData,'districtData':districtData})
    
def delplace(request,delID):
    tbl_place.objects.get(id=delID).delete()
    return redirect("Administrator:placeInsertSelect")

def editplace(request,editID):
    districtData=tbl_district.objects.all()
    ed=tbl_place.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtplace")
        ed.place_name=name
        ed.district=tbl_district.objects.get(id=request.POST.get("selDistrict"))
        ed.save()
        return redirect("Administrator:placeInsertSelect")
    else:
        return render(request,"Administrator/Place.html",{'edit':ed,'districtData':districtData})
    
#Notification

def notificationInsertSelect(request):
    if request.method == "POST":
        content = request.POST.get("txtcon")
        tbl_Notification.objects.create(notification_content=content)
        return redirect('Administrator:notificationInsertSelect')  # Redirect to clear form data

    notificationdata = tbl_Notification.objects.all()
    return render(request, 'Administrator/Notification.html', {'data': notificationdata})


#notifaction view

def notifiiew(request):

    notificationdata=tbl_Notification.objects.all()
    return render(request,'Administrator/NotificationView.html',{'data':notificationdata})





#Bloodbank section
def BloodbankInsertSelect(request):
    districtData=tbl_district.objects.all()
    bloodbankdata=tbl_bloodbank.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        contact=request.POST.get('txtphone')
        address=request.POST.get('txtname')
        district=request.FILES.get('selBloodgroup')
        password=request.POST.get('txtpwd') 
        district=tbl_district.objects.get(id=request.POST.get('selDistrict'))   
        tbl_bloodbank.objects.create(bloodbank_name=name,
                                 bloodbank_contact=contact,bloodbank_email=email,bloodbank_password=password,
                                 bloodbank_address=address,
                                 district=district)
        return render(request,'Administrator/Bloodbank.html',{'bloodbankdata':bloodbankdata,'districtData':districtData})
    else:
        return render(request,'Administrator/Bloodbank.html',{'bloodbankdata':bloodbankdata,'districtData':districtData})


def delBloodbank(request,delID):
    tbl_bloodbank.objects.get(id=delID).delete()
    return redirect("Administrator:BloodbankInsertSelect")
    
def editBloodbank(request,editID):
    ed=tbl_bloodbank.objects.get(id=editID)
    # et=tbl_bloodgroup.objects.get(id=editID)
    if request.method=="POST":
        name=request.POST.get("txtname")
        email=request.POST.get('txtemail')
        contact=request.POST.get('txtphone')
        address=request.POST.get('txtname')
        
        ed.bloodbank_name=name
        ed.bloodbank_email=email
        ed.bloodbank_contact=contact
        ed.bloodbank_address=address
        ed.save()
        return redirect("Administrator:BloodbankInsertSelect")
    else:
        return render(request,"Administrator/Bloodbank.html",{'edit':ed})
    


#DonorVerification

def DonorVerificationInsert(request):

    donorverfication=tbl_donor.objects.all()
    data=tbl_district.objects.all()

    blooddata=tbl_bloodgroup.objects.all()

    return render(request,'Administrator/DonorVerification.html',{'data':data,'blooddata':blooddata,'donorverfication':donorverfication})
    

#PatientVerification section
def PatientVerificationInsert(request):

    patientverification=tbl_patient.objects.all()
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
        return render(request,'Administrator/PatientVerification.html',{'data':data,'blooddata':blooddata,'patientverification':patientverification})
    else:
        return render(request,'Administrator/PatientVerification.html',{'data':data,'blooddata':blooddata,'patientverification':patientverification})


#home page for the admin 
def homeinsert(request):


    bloodcat = tbl_bloodgroup.objects.all()
    for i in bloodcat:
        count = tbl_blooddonate.objects.filter(donor__bloodgroup=i.id).aggregate(total=Sum("blooddonate_unit"))['total'] or 0
        req = tbl_request.objects.filter(bloodgroup=i.id,request_status=1).aggregate(total=Sum("request_quantitiy"))["total"] or 0
        total= count - req
        i.bloodcount = total


    return render(request,'Administrator/HomePage.html',{"blood":bloodcat})


#patient request data 
def patientRequestData(request):
    bloodunit=tbl_request.objects.all()
    return render(request,'Administrator/PatientRequestData.html',{'bloodunit':bloodunit})

#camp details 


def campdetails(request):
    data=tbl_camp.objects.all()
    return render(request,'Administrator/CampDetails.html',{'data':data})

#approve buttom 

def approve(request,id):
    approve=tbl_camp.objects.get(id=id)
    approve.camp_status=1
    approve.save()
    return redirect("Administrator:campdetails")

def reject(request,id):
    approve=tbl_camp.objects.get(id=id)
    approve.camp_status=2
    approve.save()
    return redirect("Administrator:campdetails")



# def bloodavailble(request):
#     group=tbl_donor.objects.all()
#     data=tbl_blooddonate.objects


def logout(request):
    del request.session["aid"]
    return redirect("Guest:index")





