from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from .models  import Kullanicilar


class testForm(forms.ModelForm):
    
    class Meta:
        model = Kullanicilar
        fields = ['__all__']


  