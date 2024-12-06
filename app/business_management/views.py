from django.shortcuts import render, redirect
from django.contrib import messages

# from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from .models import Employee

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            password = form.cleaned_data['password']
            try:
                employee = Employee.objects.get(id=employee_id, password=password)
                # ログイン成功処理
                # login(request, user)
                request.session['employee_id'] = employee.id
                # messages.success(request, f'Welcome {employee.name}')
                # return redirect('home')
                return render(request, 'business_management/home.html', {'employee': employee})
            except Employee.DoesNotExist:
                messages.error(request, 'Invalid email or password')
    else:
        params = {
            'form': LoginForm()
        }

    return render(request, 'business_management/index.html', params)


def logout_view(request):
    request.session.clear()
    request.session.flush()
    return redirect('index')


def home(request):
    employee_id = request.session.get('employee_id')

    if employee_id:
        try:
            # データベースから再度取得
            employee = Employee.objects.get(id=employee_id)
            # 必要な情報をテンプレートに渡す
            return render(request, 'business_management/home.html', {'employee': employee})
        except Employee.DoesNotExist:
            messages.error(request, 'Employee not found')
            return redirect('index')
    return redirect('index')


def register(request):
    print('register debug')
    params = {
            'form': RegisterForm()
    }
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            name = form.cleaned_data['name']
            department_obj = form.cleaned_data['department_id']
            department_id = department_obj.id
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                employee = Employee.objects.create(id=employee_id, name=name, department_id=department_id, email=email, password=password)
                employee.save()
                request.session['employee_id'] = employee.id
                # messages.success(request, f'Welcome {employee.name}')
                return redirect('home')
            except Exception as e:
                messages.error(request, e)
                return redirect('register')
    return render(request, 'business_management/register.html', params)

