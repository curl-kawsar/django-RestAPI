from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, RegistrationApiView, ActivateAccountView, UserLoginApiView, UserLogoutApiView

router = DefaultRouter()
router.register('patient', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
]