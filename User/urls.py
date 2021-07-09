from django.urls import path, include
from django_email_verification import urls as email_urls


from . import views

urlpatterns = [
    path('dashboard/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name='secret'),
    path('update-email/', views.update_email, name='update-email'),
    path('email/', include(email_urls)),
    path('createGroup/', views.create_group, name='createGroup'),
    path('groupDashboard/<str:pk>', views.group_dashboard, name='groupDash'),
    path('invite/<group_id>', views.invite, name='invite'),
    path('accept-invite/<group_id>', views.accept_invite, name='acceptinvite'),

]