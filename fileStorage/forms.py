from django import forms

from .models import fileStorageSchema
from User.models import Group, Member

class fileForm(forms.ModelForm):
    
    #groups = forms.ModelChoiceField(queryset=Group.objects.all().values_list('groupName', flat=True)) # to_field_name="groupName")#
    
    class Meta:
        
        model = fileStorageSchema
        fields = ('public', 'fileNote')