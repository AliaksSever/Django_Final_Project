from dataclasses import fields
from django.forms import ModelForm
from .models import Account

from django import forms


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'age', 'sex', 'job', 'about']


    # widgets = {
    #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
    #     'last_name': 
    # } Продолжить
 

# class TodoForm(ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['title', 'memo', 'important', 'tags']

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'memo': forms.Textarea(attrs={'class': 'form-control'}),
#             'important': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
#             'tags': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
#         }



# class TagForm(ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['title', 'slug']

#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'slug': forms.TextInput(attrs={'class': 'form-control'})
#         }
    
