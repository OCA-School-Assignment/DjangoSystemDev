from django import forms
from .models import Department
class LoginForm(forms.Form):
    """ログインフォーム"""
    employee_id = forms.CharField(
        label='従業員ID',
        min_length=8,
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'w-full p-2 border border-gray-300 rounded',})
    )
    password = forms.CharField(
        label='パスワード',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
    )


class RegisterForm(forms.Form):
    employee_id = forms.CharField(
        label='従業員ID',
        min_length=8,
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'w-full p-2 border border-gray-300 rounded',})
    )

    name = forms.CharField(
        label='名前',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
    )

    department_id = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        empty_label='None',
        initial=None,
        label='部署ID',
        widget=forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
    )

    email = forms.EmailField(
        label='メールアドレス',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
    )

    password = forms.CharField(
        label='パスワード',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
    )