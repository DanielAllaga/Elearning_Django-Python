from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student


        #fill up all column
        fields = '__all__'
        #hide professor_id field
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

