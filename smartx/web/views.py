""" This file contains the views for the landing page of the website. """
from django.shortcuts import render

# Create your views here.
def landing_page(request):
    """
    This view renders the landing page of the website.
    request: The request object used to generate this page.
    return: The rendered landing page.
    """
    return render(request, 'landing.html')
