from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        user = None

        try:
            user = User.objects.get(email=email)
        except:
            return email

        if user is not None:
            raise ValidationError('User Already Exists')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None

        try:
            user = User.objects.get(username=username)
            result = authenticate(username=user, password=password)

            if result is not None:
                login(self.request, result)

                return result
            else:
                raise ValidationError('Password Invalid')
        except:
            raise ValidationError('Email and Password are Invalid')
