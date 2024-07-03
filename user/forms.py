from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model 

User = get_user_model()

class RegisterForm(UserCreationForm):
    # username = forms.CharField(max_length=255,widget= forms.TextInput(attrs={'class':'form-control'},),label='Имя пользователя',)
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'FormInput'}), label='Пароль', help_text="Пароль не должен быть слишком похож на другую вашу личную информацию.")
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'FormInput'}), label='Подтверждение пароля', help_text= 'Для подтверждения введите, пожалуйста, пароль ещё раз.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'FormInput'},),
            'email':forms.EmailInput(attrs={'class':'FormInput'}),
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')