from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import album_image_view, success, display_album_images

urlpatterns = [
    path('image_upload', album_image_view, name='image_upload'),
    path('success', success, name='success'),
    path('album_images', display_album_images, name = 'album_images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
