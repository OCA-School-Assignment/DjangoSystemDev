from django import forms

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
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
    )