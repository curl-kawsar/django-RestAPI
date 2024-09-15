from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, ReviewViewSet, SpecializationViewSet

router = DefaultRouter()
router.register('doctor', DoctorViewSet)
router.register('reviews', ReviewViewSet)
router.register('specializations', SpecializationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]