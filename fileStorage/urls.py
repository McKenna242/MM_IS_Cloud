from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


from . import views

urlpatterns = [
    path('', views.home_redirect),
    path('fileStorage/', views.file_list, name = 'file'), #our-domain.com/fileStorage
    path('fileStorage/upload/', views.upload_file, name = 'upload'),
    path('fileStorage/delete/<str:pk>/', views.delete_file, name = 'delete'),
    path('fileStorage/player/<str:pk>', views.video_play, name = 'video'),
    path('fileStorage/image/<str:pk>', views.image_view, name = 'image'),
    path('fileStorage/pdf/<str:pk>', views.pdf_view, name = 'pdf'),
    path('fileStorage/text/<str:pk>', views.text_view, name = 'text')



    
]

#just for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)