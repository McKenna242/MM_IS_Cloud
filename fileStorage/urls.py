from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('fileStorage/', views.file_list), #our-domain.com/fileStorage
    path('fileStorage/upload/', views.upload_file)
]

#just for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)