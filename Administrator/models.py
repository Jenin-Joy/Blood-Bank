from django.db import models 

# Create your models here.
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)

class tbl_complainttype(models.Model):
    complainttype_name=models.CharField(max_length=50)


class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_bloodgroup(models.Model):
    Bloodgroup_name=models.CharField(max_length=50)
    
class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_bloodbank(models.Model):
    bloodbank_name=models.CharField(max_length=50)
    bloodbank_email=models.CharField(max_length=50)
    bloodbank_contact=models.CharField(max_length=50)
    bloodbank_address=models.CharField(max_length=50)
    bloodbank_password=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_Notification(models.Model):
    notification_date=models.DateField(auto_now_add=True)
    notification_content=models.CharField(max_length=50)
    bloodbank=models.ForeignKey(tbl_bloodbank,on_delete=models.CASCADE, null=True, blank=True)
