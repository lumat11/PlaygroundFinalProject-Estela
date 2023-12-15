from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from BlogEstadiosApp.models import Estadio, UserProfile



class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput())


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)
    description = forms.CharField(required=False)
    portfolio_link = forms.URLField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('email', 'avatar', 'description', 'portfolio_link')


class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ['name', 'apodo', 'body', 'image']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email',
                  'avatar', 'description', 'portfolio_link']
