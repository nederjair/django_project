from django import forms
from django.forms import ModelForm
from .models import AppModel

class AppForm(ModelForm):
    class Meta:
        model = AppModel
        fields = [
            'name', 'num1', 'num2'
        ]