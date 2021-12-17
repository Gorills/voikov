

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hod-stroitelstva/', views.hod_stroitelstva, name='hod_stroitelstva'),
    path('dokumentatsiya/', views.dok, name='dok'),
    path('<slug:slug>/', views.page, name='page'),
    
]
