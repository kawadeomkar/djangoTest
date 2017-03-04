from django.contrib.auth.models import User
from django import forms

class SearchForm(forms.ModelForm):
    city = forms.CharField(max_length=20)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']