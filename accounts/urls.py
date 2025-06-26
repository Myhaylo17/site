from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('achievments/', views.achievments_view, name='achievments'),
    path('logout/', views.logout_view, name='logout'),


     # Тепер це буде /home/

]

