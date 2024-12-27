""" URL Configuration for the landing_page app """
from django.urls import path
from . import views

urlpatterns = [
    # Landing Page
    path('', views.landing_page, name='landing_page'),
    # Sign In / Sign Up Page
    path('signin/', views.signin_signup, name='signin_signup'),
    # About Us Page
    path('about/', views.about_us, name='about_us'),
    # Contact Us Form
    path('contact-us/', views.contact_us, name='contact_us'),
]
