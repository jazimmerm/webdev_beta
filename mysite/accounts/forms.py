from django.forms import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'placeholder':'Enter Username', 'autocomplete':'username', 'id':'username'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'autocomplete':'new-password'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Re-enter Password', 'autocomplete':'new-password'})
        self.fields['email'].widget.attrs.update({'placeholder':'Enter Email', 'autocomplete':'off', 'id':'email', 'type':'email'})

class LoginForm(AuthenticationForm):
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = PasswordInput(
            attrs={'type':'text', 'class':'form-control', 'placeholder': 'Username', 'autocomplete':'username'})
        self.fields['password'].widget = TextInput(
            attrs={'type':'password', 'class':'form-control', 'id':'myInput', 'placeholder': 'Password', 'autocomplete':'password'})