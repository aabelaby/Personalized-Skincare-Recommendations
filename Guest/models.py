from django.db import models

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_age=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='Assets/User/Photo/')
