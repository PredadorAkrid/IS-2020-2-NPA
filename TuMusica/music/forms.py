"""Users forms."""
# Django
from django import forms
from django.contrib.auth.models import *
from .models import * 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class AddArtistForm(forms.Form):
    

    artist = forms.IntegerField()
    name = forms.CharField(max_length=200)
    image = forms.ImageField()

    def clean_name(self):
        """Validate that the name doesn't exist in the database."""
        data = self.cleaned_data["name"]
        if Artist.objects.filter(name=data).count() > 0:
            raise forms.ValidationError("This artist already exists.")
        
        return data
