from django import forms
from .models import ToDo

class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'due_date', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description...'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        
class QuickAddForm(forms.ModelForm):
    """Simplified form for quick task addition"""
    class Meta:
        model = ToDo
        fields = ['name', 'due_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'What needs to be done?',
                'required': True
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        