from os import name
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class GetInTouch(models.Model):
    name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True, editable=True)
    @classmethod
    def get_in_touch(cls):
        return cls.objects.filter(name="name")
    def save_get_in(self):
        self.save()
        
class Testmonials(models.Model):
    name = models.CharField(max_length=30)
    image = CloudinaryField('image')
    position = models.TextField(null=True)
    testmony = models.TextField(null=True)
    approve = models.BooleanField(default=False,null=True)
    created_at = models.DateField(auto_now_add=True, editable=True)
    @classmethod
    def get_all_approved(cls):
        return cls.objects.filter(approve=True)
    def saving(self):
        self.save()
