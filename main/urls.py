from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),   
    path('about/', views.about, name='about'),
    path('', views.welcome, name='welcome'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),

]
