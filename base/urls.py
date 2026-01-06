from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('become-client/', views.become_client, name='become_client'),
    path('contact/', views.contact, name='contact'),
    path('room/<str:pk>/', views.room, name='room'),  # je oude room route
]