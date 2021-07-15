from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Group, ChangeEmail


def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError(
            (f"{value} is currently in use. Please enter a valid email Address."),
            params = {'value':value}
        )
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(validators = [validate_email], max_length=254, help_text = 'Required to enter a valid email address.')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
class UserForm(forms.ModelForm):
      #email = forms.EmailField(validators = [validate_email], max_length=254, help_text = 'Enter a valid email address')
      class Meta:
        model = User
        fields = ['first_name', 'last_name']

class EmailForm(forms.ModelForm):
    email = forms.EmailField(validators = [validate_email], max_length=254, help_text = 'Enter a valid email address')
    class Meta:
        model = ChangeEmail
        fields = ['email']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['groupName']
        
class InviteForm(forms.Form):
    users = forms.ModelChoiceField(queryset=User.objects.all())