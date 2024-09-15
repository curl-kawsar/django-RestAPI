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

#custom router
class CustomRouter(DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)
        
        # URLs
        api_root_dict['register'] = 'register'
        api_root_dict['login'] = 'login'
        api_root_dict['logout'] = 'logout'

        class APIRoot(APIView):
            def get(self, request, *args, **kwargs):
                return Response(OrderedDict(
                    (key, reverse(url_name, request=request, format=kwargs.get('format')))
                    for key, url_name in api_root_dict.items()
                ))

        return APIRoot.as_view()

#main router
router = CustomRouter()


from contact.urls import router as contact_router
from service.urls import router as service_router
from appointment.urls import router as appointment_router
from patient.urls import router as patient_router
from doctor.urls import router as doctor_router

#Extend the main router with routers
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
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
