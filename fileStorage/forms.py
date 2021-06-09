from django import forms

from .models import fileStorageSchema

class fileForm(forms.ModelForm):
    class Meta:
        model = fileStorageSchema
        fields = ('public', 'fileNote')