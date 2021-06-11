from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('fileStorage/', views.file_list, name = 'file'), #our-domain.com/fileStorage
    path('fileStorage/upload/', views.upload_file, name = 'upload'),
    path('fileStorage/delete/<str:pk>/', views.delete_file, name = 'delete'),
    path('fileStorage/player/<str:pk>', views.video_play, name = 'video')

]

#just for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)