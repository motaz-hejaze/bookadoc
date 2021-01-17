from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=UserModel.USER_TYPES)
    class Meta:
        model = UserModel
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    user_type = forms.ChoiceField(choices=UserModel.USER_TYPES)
    class Meta:
        model = UserModel
        fields = '__all__'