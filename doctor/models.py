from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient 
# Create your models here.


class Specialization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Designation(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name
    
class AvailableTime(models.Model):
    time = models.TimeField()
    
    def __str__(self):
        return str(self.time)
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(upload_to='doctor/images/')
    specialization = models.ManyToManyField(Specialization)
    designation = models.ManyToManyField(Designation)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=200)
    def __str__(self):
        return f"Dr. {self.user.first_name}  {self.user.last_name}"
    
    class Meta:
        verbose_name_plural = 'Doctors'
        
        
        
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
        
class Review(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=5)
    
    def __str__(self):
        return f"Patient: {self.patient.first_name} to Doctor: {self.doctor.user.first_name}"
    
    class Meta:
        verbose_name_plural = 'Reviews'