from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'username', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise ValidationError('Usuario o contraseña incorrectos')
    




