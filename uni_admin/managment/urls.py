from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact')
]

