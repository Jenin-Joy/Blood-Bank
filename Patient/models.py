from django.db import models
from Guest.models import *
from Administrator.models import *

# Create your models here.

class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)
    request_quantitiy=models.CharField(max_length=50)
    request_fordate=models.CharField(max_length=50)
    patient=models.ForeignKey(tbl_patient,on_delete=models.CASCADE)
    bloodgroup=models.ForeignKey(tbl_bloodgroup,on_delete=models.CASCADE)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    request_location=models.CharField(max_length=50)
    donor = models.ForeignKey(tbl_donor,on_delete=models.CASCADE, null=True)


