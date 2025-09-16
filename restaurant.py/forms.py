from django import forms
from .models import contact

class ConatactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email']