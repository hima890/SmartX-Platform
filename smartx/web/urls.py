""" URL Configuration for the landing_page app """
from django.urls import path
from . import views

urlpatterns = [
    # Landing Page
    path('', views.landing_page, name='landing_page'),
]
