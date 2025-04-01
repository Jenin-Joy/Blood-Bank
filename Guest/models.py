from django.db import models
from Administrator.models import *
# Create your models here.

class tbl_donor(models.Model):
    donor_name=models.CharField(max_length=50)
    donor_email=models.CharField(max_length=50)
    donor_contact=models.CharField(max_length=50)
    donor_address=models.CharField(max_length=50)
    donor_status=models.IntegerField(default=0)
    donor_photo=models.FileField(upload_to='Assets/File/Donor/')
    donor_password=models.CharField(max_length=50)
    
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    bloodgroup=models.ForeignKey(tbl_bloodgroup,on_delete=models.CASCADE)
    disease_status=models.CharField(max_length=50)
    donor_age=models.CharField(max_length=50)

class tbl_patient(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_email=models.CharField(max_length=50)
    patient_contact=models.CharField(max_length=50)
    patient_address=models.CharField(max_length=50)
    patient_photo=models.FileField(upload_to='Assets/File/Donor/')
    patient_password=models.CharField(max_length=50)

    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    bloodgroup=models.ForeignKey(tbl_bloodgroup,on_delete=models.CASCADE)
    patient_status=models.IntegerField(default=0)
    patient_age=models.CharField(max_length=50)





