from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')),
    path('', include('service.urls')),
    path('', include('appointment.urls')),
    path('', include('patient.urls')),
    # path('', include('doctor.urls')),  # This will include the doctor app's urls
    path('', include('doctor.urls')),  # Add this line to include the API routes
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)