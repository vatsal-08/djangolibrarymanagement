from django import forms
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widgets=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password", widgets=forms.PasswordInput)

    class Meta:
        model = User

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 == password2:
            return password2
        raise forms.ValidationError("Passwords don't match")

    def save(self, commit=True):
        user = super().save(commit=False)
