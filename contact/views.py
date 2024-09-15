from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import ContactUs
from . import serializers
from . import models


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer