from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import LoginForm
from ..models import Employee, Department, Order


def index(request):
    params = {
        'form': LoginForm(),
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            password = form.cleaned_data['password']
            try:
                employee = Employee.objects.get(id=employee_id, password=password)
                print(f"従業員名: {employee}")
                request.session['employee_name'] = employee.name
                request.session['employee_id'] = employee.id
                return redirect('home')
            except Employee.DoesNotExist:
                messages.error(request, 'メールアドレスまたはパスワードが間違っています。')
        else:
            redirect('index')
    return render(request, 'business_management/index.html', params)


def logout_view(request):
    request.session.clear()
    request.session.flush()
    return redirect('index')


def home(request):
    employee_id = request.session.get('employee_id')

    employee = Employee.objects.get(id=employee_id)
    department = Department.objects.get(id=employee.department_id) 
    request.session['employee_name'] = employee.name
    request.session['department_name'] = department.name
    return render(request, 'business_management/home.html')


def test(request):
    orders = Order.objects.all()
    return render(request, 'business_management/test.html', {'orders': orders})
