from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class UtilisateurForm(forms.Form):
    nom = forms.CharField(max_length=100)


