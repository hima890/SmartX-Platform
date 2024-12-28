"""Models for the app."""
from django.db import models
from django.core.validators import validate_email


# Contact Form Model
class ContactForm(models.Model):
    """Model for the contact form."""
    name = models.CharField(max_length=100) # max_length is required
    email = models.EmailField(validators=[validate_email]) # EmailField is a field for email
    message = models.TextField() # TextField is a field for large text
    # auto_now_add sets the field to now when the object is created
    created_at = models.DateTimeField(auto_now_add=True) 


    # String representation of the model
    def __str__(self):
        return "name: " + self.name + " email: " + self.email
