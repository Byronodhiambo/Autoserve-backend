from django.urls import path, include
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views

urlpatterns = [
     path('register/', RegisterAPI.as_view(), name='register'),
     path('login/', LoginAPI.as_view(), name='login'),
     path('logout/', LoginAPI.as_view(), name='logout'),
     path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
     path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]