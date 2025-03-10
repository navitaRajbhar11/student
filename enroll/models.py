from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    Profile_Images = models.ImageField(upload_to='student_images/',null=True,blank=True)