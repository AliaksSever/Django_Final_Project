from dataclasses import fields
from django.forms import ModelForm
from .models import Todo, Tag

from django import forms

from django.core.exceptions import ValidationError

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'memo': forms.Textarea(attrs={'class': 'form-control'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
        }



class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }
    

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug should be UNIQE. We already have "{new_slug}"')
        return new_slug