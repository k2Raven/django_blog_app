from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

# class MyUserCreationForm(forms.ModelForm):
#     password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput, strip=False)
#     password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput,
#                                        strip=False)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirm = cleaned_data.get('password_confirm')
#         if password_confirm != password:
#             raise forms.ValidationError('Пароли не совпадают!')
#         return cleaned_data
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data.get('password'))
#         if commit:
#             user.save()
#         return user
#
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']
