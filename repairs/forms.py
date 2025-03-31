from django import forms
from .models import RepairRequest

class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['name', 'phone', 'device_type', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'device_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
