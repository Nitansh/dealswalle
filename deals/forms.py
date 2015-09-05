from django import forms
from django.forms import ModelForm
from .models import CustomerQuery

class QueryForm(ModelForm):
    class Meta:
        model = CustomerQuery