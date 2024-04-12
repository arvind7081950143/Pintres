from django.db import models
from item.models import Item
from django.contrib.auth.models import User

class Profile_user(models.Model):
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    name = models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=1500)
    github=models.CharField(max_length=250)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    name = models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=1500)
    github=models.CharField(max_length=250)
    twitter=models.CharField(max_length=250)
    file=models.FileField(upload_to='profile',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# Create your models here.
