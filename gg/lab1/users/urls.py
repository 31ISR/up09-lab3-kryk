from django.contrib import admin
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='reg'),
    path('login/', views.login_view, name='log')
]