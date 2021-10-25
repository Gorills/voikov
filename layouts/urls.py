

from django.urls import path
from . import views

urlpatterns = [
    path('', views.layouts, name='layouts'),
    path('<slug:slug>/', views.layouts_detail, name='layouts_detail'),
    path('room/<slug:slug>/', views.room, name='room')
    
  
]
