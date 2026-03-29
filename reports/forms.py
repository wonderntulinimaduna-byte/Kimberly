from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['category', 'description', 'location', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe the problem briefly'}),
        }