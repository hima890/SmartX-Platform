"""" This file is used to create a form for the ContactForm model. """
from django import forms
from .models import ContactForm


class ContactFormForm(forms.ModelForm):
    """"
    This class creates a form for the ContactForm model.
    """
    class Meta:
        """
            This class contains metadata for the form.
        """
        model = ContactForm
        fields = ['name', 'email', 'message']

    def clean_email(self):
        """Clean the email field.

        Raises:
            forms.ValidationError: If the email does not end with '@example.com'.

        Returns:
            _type_: The cleaned email strng.
        """
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Please use an @example.com email address.')
        return email
