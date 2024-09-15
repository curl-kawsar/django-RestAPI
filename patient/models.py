from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200,blank=True, null=True)
    iamge = models.ImageField(upload_to='patient/images/')
    mobile = models.CharField(max_length=15)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"