
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('choise/', include('layouts.urls')),
    path('admin/', admin.site.urls),
    path('calback/', include('contacts.urls')),
    
    path('', include('vojkov.urls')),
    
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)