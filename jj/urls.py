from django.contrib import admin
from django.urls import path,include
from jj import views

urlpatterns = [
    path('',views.jj,name="home"),
    path('events',views.events,name="envents"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('cou',views.cou,name="cou"),
    path('course',views.course,name="course"),
    path('trainer',views.trainer,name="trainer")
]
