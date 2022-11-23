from django.db import models
class post(models.Model):
    image1=models.ImageField (upload_to="images")
    image2=models.ImageField(upload_to="images")
    image3=models.ImageField(upload_to="images",default="")
    title1=models.CharField(max_length=500,default="")
    title2=models.CharField(max_length=500,default="")
    title3=models.CharField(max_length=500,default="")
    p1=models.CharField(max_length=400,default="")
    p2=models.CharField(max_length=400,default="")
    p3=models.CharField(max_length=400,default="")
    sh1=models.CharField(max_length=200,default="")
    sh2=models.CharField(max_length=200,default="")
    sh3=models.CharField(max_length=200,default="")

# Create your models here.
class posts(models.Model):
    image1=models.ImageField (upload_to="images")
    image2=models.ImageField(upload_to="images")
    image3=models.ImageField(upload_to="images",default="")
    image4=models.ImageField (upload_to="images")
    image5=models.ImageField (upload_to="images")
    title1=models.CharField(max_length=500,default="")
    title2=models.CharField(max_length=500,default="")
    title3=models.CharField(max_length=500,default="")
    title4=models.CharField(max_length=500,default="")
    title5=models.CharField(max_length=500,default="")
    p1=models.CharField(max_length=400,default="")
    p2=models.CharField(max_length=400,default="")
    p3=models.CharField(max_length=400,default="")
    p4=models.CharField(max_length=400,default="")
    p5=models.CharField(max_length=400,default="")
    h1=models.CharField(max_length=200,default="")
    h2=models.CharField(max_length=200,default="")
    h3=models.CharField(max_length=200,default="")
    h4=models.CharField(max_length=200,default="")
    h5=models.CharField(max_length=200,default="")
    h5=models.CharField(max_length=200,default="")
     
     # Create your models here.
class event(models.Model):
    image1=models.ImageField (upload_to="images")
    image2=models.ImageField(upload_to="images")

    h1=models.CharField(max_length=500,default="")
    h2=models.CharField(max_length=500,default="")
   
    p1=models.CharField(max_length=400,default="")
    p2=models.CharField(max_length=400,default="")
    
    p3=models.CharField(max_length=200,default="")
    p4=models.CharField(max_length=200,default="")

class train (models.Model):
    image1=models.ImageField (upload_to="images")
    image2=models.ImageField(upload_to="images")
    image3=models.ImageField(upload_to="images",default="")
    h1=models.CharField(max_length=500,default="")
    h2=models.CharField(max_length=500,default="")
    h3=models.CharField(max_length=500,default="")
    p1=models.CharField(max_length=400,default="")
    p2=models.CharField(max_length=400,default="")
    p3=models.CharField(max_length=400,default="")
    sh1=models.CharField(max_length=200,default="")
    sh2=models.CharField(max_length=200,default="")
    sh3=models.CharField(max_length=200,default="")
