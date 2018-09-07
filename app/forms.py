from django import forms
from .models import bank,b_city

class bankForm(forms.ModelForm):
    class Meta:
        model=bank
        fields=['ifsc']

class b_cityForm(forms.ModelForm):
    class Meta:
        model=b_city
        fields=['city','b_name']