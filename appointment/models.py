from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime

# Create your models here.

APPOINTMENT_TYPE = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),
)

APPOINTMENT_STATUS = (
    ('Pending', 'Pending'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=APPOINTMENT_TYPE, max_length=10)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS, max_length=10, default='Pending')
    symptoms = models.TextField()
    time = models.OneToOneField(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    date = models.DateField(default=None)
    
    def __str__(self):
        return f"Doctor: {self.doctor.first_name}, Patient: {self.patient.first_name}"

    class Meta:
        verbose_name_plural = 'Appointments'