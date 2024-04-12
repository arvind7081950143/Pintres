from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    description=models.CharField(max_length=2000)
    def __str__(self):
        return self.name

# Create your models here.
