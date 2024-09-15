from rest_framework import serializers
from .models import Doctor, Specialization, Designation, AvailableTime, Review

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['name', 'slug']
        read_only_fields = ['name', 'slug']

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['name', 'slug']
        read_only_fields = ['name', 'slug']

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = ['time']
        read_only_fields = ['time']

class DoctorSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(many=True, read_only=True)
    designation = DesignationSerializer(many=True, read_only=True)
    available_time = AvailableTimeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Doctor
        fields = ['user', 'first_name', 'last_name', 'image', 'specialization', 'designation', 'available_time', 'fee', 'meet_link']
        read_only_fields = ['user', 'first_name', 'last_name', 'image', 'specialization', 'designation', 'available_time', 'fee', 'meet_link']
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['patient', 'doctor', 'review', 'created', 'rating']
        read_only_fields = ['created']