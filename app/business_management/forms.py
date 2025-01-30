from django import forms
from .models import Department, Employee, Items, Production, Order, Customer
from django.core.exceptions import ValidationError

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


class EmployeeRegisterForm(forms.Form):
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


class EmployeeSearchForm(forms.Form):
    search_type_choices = [
        ('id', '従業員ID'),
        ('name', '従業員名'),
    ]
    search_type = forms.ChoiceField(choices=search_type_choices, required=True)
    query = forms.CharField(max_length=100, required=False)


class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'department': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'password': forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
        }

class DepartmentRegisterForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'autofocus': True, 'class': 'w-full p-2 border border-gray-300 rounded',})
        }   

class DepartmentEditForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
        }


class StockSearchForm(forms.Form):
    search_type_choices = [
        ('item_id', '製品ID'),
        ('name', '製品名'),
    ]
    search_type = forms.ChoiceField(choices=search_type_choices, required=True)
    query = forms.CharField(max_length=100, required=False)

class ProductSearchForm(forms.Form):
    search_type_choices = [
        ('id', '製品ID'),
        ('name', '製品名'),
    ]
    search_type = forms.ChoiceField(choices=search_type_choices, required=True)
    query = forms.CharField(max_length=100, required=False)


class ProductRegisterForm(forms.Form):
    product_id = forms.CharField(
        label='製品ID',
        min_length=8,
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'w-full p-2 border border-gray-300 rounded',})
    )

    product_name = forms.CharField(
        label='製品名',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
    )

    price = forms.IntegerField(
        label='製品単価',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',})
    )

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
        }


class ShipmentLogSearchForm(forms.Form):
    search_type_choices = [
        ('item_id', '製品ID'),
        ('name', '製品名'),
    ]
    search_type = forms.ChoiceField(choices=search_type_choices, required=True)
    query = forms.CharField(max_length=100, required=False)


class ProductionRegisterForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['order', 'lot_quantity', 'due_date', 'estimated_completion_date', 'completion_date']
        widgets = {
            'order': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'lot_quantity': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'due_date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'type': 'date'}),
            'estimated_completion_date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'type': 'date'}),
            'completion_date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'type': 'date'}),
            }
        
        completion_date = forms.DateField(
            required=False,
            widget=forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'type': 'date'}),
        )

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise ValidationError('数量は1以上の整数を入力してください。')
        return quantity
    

class ProductionEditForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['lot_quantity', 'due_date', 'estimated_completion_date', 'completion_date']
        widgets = {
            'lot_quantity': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'due_date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'estimated_completion_date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'completion_date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise ValidationError('数量は1以上の整数を入力してください。')
        return quantity
    

class ProductionSearchForm(forms.Form):
    query = forms.IntegerField(
        label='製造ID', 
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': '製造ID',}))
    

class CustomerSearchForm(forms.Form):
    search_type_choices = [
        ('id', '得意先ID'),
        ('name', '得意先名'),
    ]
    search_type = forms.ChoiceField(choices=search_type_choices, required=True)
    query = forms.CharField(max_length=100, required=False)


class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'contact_number', 'postal_code', 'address']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'contact_number': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'postal_code': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'address': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
        }


class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'contact_number', 'postal_code', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'contact_number': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'postal_code': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
            'address': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded',}),
        }