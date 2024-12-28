""" This file contains the views for the landing page of the website. """
from django.shortcuts import render, redirect, HttpResponse
from .form import ContactFormForm


# Create your views here.
def landing_page(request):
    """
    This view renders the landing page of the website.
    request: The request object used to generate this page.
    return: The rendered landing page.
    """
    return render(request, 'index.html')


def signin_signup(request):
    """
    This view renders the sign in / sign up page of the website.
    request: The request object used to generate this page.
    return: The rendered sign in / sign up page.
    """
    return render(request, 'forms.html')


def about_us(request):
    """
    This view renders the about us page of the website.
    request: The request object used to generate this page.
    return: The rendered about us page.
    """
    return render(request, 'about.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return HttpResponse("Form successfully saved!")
            
        else:
            return HttpResponse("Form submission failed. Please check the inputs.", status=400)
    else:
        HttpResponse("Invalid request method.", status=405)
