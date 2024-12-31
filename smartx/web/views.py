""" This file contains the views for the landing page of the website. """
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
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


@csrf_exempt
def contact_us(request):
    """
    This view handles the contact form submission.
    
    Keyword arguments:
    request -- the request
    Return: JsonResponse
    """
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved")
            return JsonResponse(
                {
                    'status': 'success',
                    'message': 'Thank you! Your message has been sent.'
                }
            )
        else:
            return JsonResponse(
                {
                    'status': 'error',
                    'message': 'Form validation failed. Please check your inputs.'
                }
            )
    return JsonResponse(
        {
            'status': 'error',
            'message': 'Invalid request method.'
        }
    )
