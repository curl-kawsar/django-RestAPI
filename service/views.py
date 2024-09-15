from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Service
from . import serializers
from . import models


class ServiceSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = serializers.SerivceSerializer