from django import forms
from .models import Disruption

class DisruptionForm(forms.ModelForm):
    class Meta:
        model = Disruption
        fields = ['author', 'description', 'category', 'section', 'lotnum', 'time']
        widgets = {
            'category': forms.RadioSelect,
            'section': forms.RadioSelect,
        }
