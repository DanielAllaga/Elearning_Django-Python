from django.forms import ModelForm
from django import forms
from .models import Class

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class

        #fill up all column
        fields = '__all__'
        #hide professor_id field
        widgets = {
            'professor': forms.HiddenInput(),
            'unique_code': forms.HiddenInput(),
            'class_code': forms.TextInput(attrs={'class': 'form-control'}),
            'class_description': forms.TextInput(attrs={'class': 'form-control'}),
            'class_section': forms.TextInput(attrs={'class': 'form-control'}),
        }

        #fill up specific column
        #fields = ['class_code', 'class_description']