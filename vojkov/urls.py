

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('dokumentatsiya/', views.dok, name='dok'),
    path('<slug:slug>/', views.page, name='page'),
    
]
