from django.db import models
from Guest.models import *
from Administrator.models import *
# Create your models here.


class tbl_camp(models.Model):
    camp_date=models.DateField()
    camp_status=models.IntegerField(default=0)
    camp_details=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    bloodbank=models.ForeignKey(tbl_bloodbank,on_delete=models.CASCADE)
    
