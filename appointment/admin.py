from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'time', 'get_status']
    list_filter = ['appointment_status']
    search_fields = ['patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name']

    def get_status(self, obj):
        return obj.appointment_status
    get_status.short_description = 'Status'

admin.site.register(Appointment, AppointmentAdmin)