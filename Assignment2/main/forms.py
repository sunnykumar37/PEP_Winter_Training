from django import forms
from .models import UserRegistration, Contact

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['name', 'email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
