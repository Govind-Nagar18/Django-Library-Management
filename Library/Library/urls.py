from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse 

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "Backend is running"})), 
    path('api/', include('Library.books.urls')),
    path('auth/', include('Library.custom_auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
