from django.urls import path, include


from . import views

urlpatterns = [
    path('dashboard/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name='secret'),
    path('update-email/', views.update_email, name='update-email'),


]