from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': "Имя пользователя"})
        self.fields['username'].label = ""
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': "Эл-почта"})
        self.fields['email'].label = ""
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "Пароль"})
        self.fields['password1'].label = ""
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "Подтвердите пароль"})
        self.fields['password2'].label = ""

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': "Имя пользователя"})
        self.fields['username'].label = ""
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': "Пароль"})
        self.fields['password'].label = ""


class EditProfile(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': "Имя"})
        self.fields['first_name'].label = ""
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': "Фамилия"})
        self.fields['last_name'].label = ""
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': "Эл-почта"})
        self.fields['email'].label = ""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
