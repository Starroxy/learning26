from django import forms
from .models import employee,course,college,ShopProduct

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields="__all__"
       
class CourseForm(forms.ModelForm):
    class Meta:
        model=course
        fields="__all__"

class collegeform(forms.ModelForm):
    class Meta:
        model=college
        fields="__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model=ShopProduct
        fields="__all__"