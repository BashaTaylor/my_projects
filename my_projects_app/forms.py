from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'technology_used', 'deployed_link']
        labels = {
            'technology_used': 'Technology Used',
        }
