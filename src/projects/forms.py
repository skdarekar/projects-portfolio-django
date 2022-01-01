from django import forms
from django.forms import widgets
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project;
        fields = ['title', 'description']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
        }