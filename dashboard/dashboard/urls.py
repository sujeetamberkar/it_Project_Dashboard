# dashboard/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static helper

urlpatterns = [
    path("admin/", admin.site.urls),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
]

# This is for development only!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
