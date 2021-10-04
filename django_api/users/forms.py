from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
    '''
        Formulaire qui intègre UserCreationForm pour gérer la création d'un utilisateur.
    '''
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Votre prénom'}))
    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Votre Nom'}))
    username = forms.CharField(max_length=254, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=30, required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(max_length=30, required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirmez votre mot de passe'}))

    token = forms.CharField(
        widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    '''
        Formulaire de base pour le profil de l'utilisateur qui étend le modèle d'utilisateur de Django.
    '''
    address = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    county = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('address', 'town', 'county', 'post_code', 'country', 'longitude', 'latitude')

class AuthForm(AuthenticationForm):
    '''
        Formulaire qui utilise l'AuthenticationForm intégré pour gérer l'authentification des utilisateurs.
    '''
    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))

    class Meta:
        model = User
        fields = ('username', 'password')