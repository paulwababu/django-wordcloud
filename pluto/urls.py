from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test, name='home'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
]

