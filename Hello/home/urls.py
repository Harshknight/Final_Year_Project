from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('',views.login_view, name='login'),
    path("home/", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact/", views.contact, name='contact'), 
    path('logout/',views.logout_view, name='logout'),
]