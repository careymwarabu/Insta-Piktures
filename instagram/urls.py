from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insta.urls')),
    
    path('accounts/register/', 
         RegistrationView.as_view(success_url='/create_profile'),
         name='django_registration_register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('logout/', auth_views.LogoutView.as_view()), 
    path('accounts/logout',LogoutView.as_view(redirect_field_name ='/accounts/login'))
]
