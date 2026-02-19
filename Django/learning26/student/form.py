from django import forms
from .models import Student,service

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class ServiceForm(forms.ModelForm):
    class Meta:
        model = service
        fields = '__all__'

    error_messages = {
        'serviceName': {
            'required': 'Add Service Name',
        },
        'servicePrice': {
            'required': 'Price is required',
        },
        'categoryid': {
            'required': 'Select a category',
        },
    }