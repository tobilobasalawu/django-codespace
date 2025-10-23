from django import forms
from .models import tblProperty

class PropertyForm(forms.ModelForm):
    class Meta:
        model = tblProperty
        fields = ['PropertyHouseNumber', 'PropertyPostcode',  'Bedrooms']#'PropertyTypeID',
        field_order = ['PropertyHouseNumber', 'PropertyPostcode',  'Bedrooms']#'PropertyTypeID',
        labels = {
            'PropertyHouseNumber': 'House Number',
            'PropertyPostcode': 'Postcode',
            #'PropertyTypeID': 'Property Type',
            'Bedrooms': 'Number of Bedrooms'
        }
        widgets = {
            'PropertyHouseNumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'PropertyPostcode': forms.TextInput(attrs={'class': 'form-control'}),
            #'PropertyTypeID': forms.Select(attrs={'class': 'form-control'}),
            'Bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
        }