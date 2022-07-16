from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'bio', 'phone_number', 'gender', 'profile_picture')
