from django.contrib import admin
from django.urls import path, include 
from home import views

# Django admin Headder Customization

admin.site.site_header="Login Interface"
admin.site.site_title="Welcome to KARAN SHARMA Dashboard"
admin.site.index_title="Welcome to this KARAN SHARMA Portal"

urlpatterns = [

    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),

]