from django.db import models

# Create your models here.
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)

class tbl_concern(models.Model):
    concern_name=models.CharField(max_length=30)
    concern_details=models.CharField(max_length=50)
    concern_photo=models.FileField(upload_to='Assets/Concern/Image/')

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_agelimit(models.Model):
    age_limit=models.CharField(max_length=30)

class tbl_gender(models.Model):
    gender=models.CharField(max_length=30)

class tbl_news(models.Model):
    news_content=models.CharField(max_length=30)
    news_photo=models.FileField(upload_to='Assets/News/Image/')

class tbl_info(models.Model):
     question=models.CharField(max_length=30)
     answer=models.CharField(max_length=30)

class tbl_skintype(models.Model):
    skin_type=models.CharField(max_length=30) 

class tbl_product(models.Model):
    product_name=models.CharField(max_length=30)
    product_price=models.CharField(max_length=30)
    product_details=models.CharField(max_length=30)
    product_amzonlink=models.CharField(max_length=60)
    product_flpctlink=models.CharField(max_length=60)
    concern=models.ForeignKey(tbl_concern,on_delete=models.CASCADE,null=True)

class tbl_skinproduct(models.Model):
    skinproduct_type=models.ForeignKey(tbl_skintype,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    

class tbl_productskintype(models.Model):
    product_skintype=models.ForeignKey(tbl_skintype,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    gallery_image=models.FileField(upload_to='Assets/Product/Image/')
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)