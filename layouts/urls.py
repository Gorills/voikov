

from django.urls import path
from . import views

urlpatterns = [
    path('', views.layouts, name='layouts'),
    
  
]
