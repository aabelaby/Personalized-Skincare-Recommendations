from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_userconcern(models.Model):
    concern=models.ForeignKey(tbl_concern,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    title=models.CharField(max_length=100)  
    content=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
