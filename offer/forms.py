from django import forms
from django.core.exceptions import ValidationError
from offer.models import *



class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['title', 'slug', 'body','img']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        return new_slug
