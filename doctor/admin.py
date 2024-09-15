from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.AvailableTime)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Specialization, SpecializationAdmin)
admin.site.register(models.Designation, DesignationAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'fee']
    filter_horizontal = ('specialization', 'designation', 'available_time')

admin.site.register(models.Doctor, DoctorAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'rating', 'created']

admin.site.register(models.Review, ReviewAdmin)