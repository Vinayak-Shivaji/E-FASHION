from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=100,null=True,blank=False)
    cat_img=models.ImageField(upload_to='image',null=True,blank=False)
    cat_des=models.CharField(max_length=200,null=True,blank=False)


SIZE_CHOICES = (
    ('S','SMALL'),
    ('M', 'MEDIUM'),
    ('L','LARGE'),
    ('XL','EXTRA LARGE'),
)
class Product(models.Model):
    pro_name=models.CharField(max_length=100,null=True,blank=False)
    pro_size=models.CharField(max_length=2, choices=SIZE_CHOICES, default='S')
    pro_price=models.CharField(max_length=100,null=True,blank=False)
    pro_cat=models.CharField(max_length=100,null=True,blank=False)
    pro_img=models.ImageField(upload_to='image',null=True,blank=False)


class User1(models.Model):
    username1=models.CharField(max_length=100,null=True,blank=False)
    password1=models.CharField(max_length=100,null=True,blank=False)
    phone1=models.CharField(max_length=100,null=True,blank=False)
    email1=models.CharField(max_length=100,null=True,blank=False)

class Cart(models.Model):
    productid=models.ForeignKey(Product,on_delete=CASCADE,null=True,blank=False)
    userid=models.ForeignKey(User1,on_delete=CASCADE,null=True,blank=False)
    total=models.IntegerField(null=True,blank=False)
    quantity=models.IntegerField(null=True,blank=False)
    status=models.IntegerField(null=True,blank=False)

class Bill(models.Model):
    cartid=models.ForeignKey(Cart,on_delete=CASCADE,null=True,blank=False)
    Fname=models.CharField(max_length=100,null=True,blank=False)
    Lname=models.CharField(max_length=100,null=True,blank=False)
    email=models.CharField(max_length=100,null=True,blank=False)
    mobile=models.IntegerField(null=True,blank=False)
    address1=models.CharField(max_length=100,null=True,blank=False)
    address2=models.CharField(max_length=100,null=True,blank=False)
    city=models.CharField(max_length=100,null=True,blank=False)
    state=models.CharField(max_length=100,null=True,blank=False)
    zip=models.IntegerField(null=True,blank=False)


class Contact(models.Model):
    name=models.CharField(max_length=100,null=True,blank=False)
    emailid=models.CharField(max_length=100,null=True,blank=False)
    subject=models.CharField(max_length=100,null=True,blank=False)
    message=models.CharField(max_length=100,null=True,blank=False)
    




    
