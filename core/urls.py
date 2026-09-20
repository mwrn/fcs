from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('matches/', views.matches_view, name='matches'),
    path('squad/', views.squad_view, name='squad'),
    path('news/', views.news_view, name='news'),
    path('contact/', views.contact_view, name='contact'),
]