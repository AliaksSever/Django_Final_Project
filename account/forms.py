from dataclasses import fields
from django.forms import ModelForm
from .models import Account

from django import forms


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'age', 'sex', 'job', 'about']


        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'job': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'})
        }