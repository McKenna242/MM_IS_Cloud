from django.urls import path

from . import views

urlpatterns = [
    path('fileStorage/', views.index) #our-domain.com/fileStorage
]