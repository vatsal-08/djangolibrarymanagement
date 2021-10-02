from django import forms
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widgets=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password", widgets=forms.PasswordInput)

    class Meta:
        model = User
