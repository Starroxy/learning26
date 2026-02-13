from django import forms
from .models import serivce

class serviceform(forms.ModelForm):
    class Meta:
        model = serivce
        fields = '__all__'
