from django import forms
from .models import Work, Client


class WorkForm(forms.ModelForm):
    
    class Meta:
        model = Work
        fields = '__all__'


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

