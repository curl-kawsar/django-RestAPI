from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from collections import OrderedDict
from patient.views import RegistrationApiView, UserLoginApiView, UserLogoutApiView, ActivateAccountView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


from contact.urls import router as contact_router
from service.urls import router as service_router
from appointment.urls import router as appointment_router
from patient.urls import router as patient_router
from doctor.urls import router as doctor_router


class CustomRouter(DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)
        

        api_root_dict['register'] = 'register'
        api_root_dict['login'] = 'login'
        api_root_dict['logout'] = 'logout'

        class APIRoot(APIView):
            def get(self, request, *args, **kwargs):
                return Response(api_root_dict)

        return APIRoot.as_view()


schema_view = get_schema_view(
    openapi.Info(
        title="Doctor Appointment API",
        default_version='v1',
        description="API documentation for Doctor Appointment",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="knownaskawsar@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = CustomRouter()

router.registry.extend(contact_router.registry)
router.registry.extend(service_router.registry)
router.registry.extend(appointment_router.registry)
router.registry.extend(patient_router.registry)
router.registry.extend(doctor_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', RegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
