from django import forms
from .models import myModel
from django.forms import ModelForm

class myForm(ModelForm):
    class Meta:
        model = myModel
        fields = ['name', 'email', 'quote_text', 'category', 'additional_details']


        category_choices = {
            ('Insurance Car Accident', 'Insurance Car Accident'),
            ('Insurance Car Damage', 'Insurance Car Damage'),
            ('Insurance Car Theft', 'Insurance Car Theft'),
            ('Insurance Car Fire', 'Insurance Car Fire'),
            ('Insurance Car Flood', 'Insurance Car Flood'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'quote_text': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=category_choices),
            'additional_details': forms.Textarea(attrs={'class': 'form-control'}),
        }

        field_order = ['name', 'email', 'quote_text', 'category', 'additional_details']