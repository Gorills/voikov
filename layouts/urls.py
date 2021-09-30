

from django.urls import path
from . import views

urlpatterns = [
    path('', views.layouts, name='layouts'),
    path('<slug:slug>/', views.layouts_detail, name='layouts_detail'),
    
  
]
