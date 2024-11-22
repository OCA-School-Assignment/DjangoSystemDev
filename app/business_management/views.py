from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import Employee

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            password = form.cleaned_data['password']
            #カスタム認証ロジック
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
        form = LoginForm()

    return render(request, 'business_management/index.html', {'form': form})


def logout_view(request):
    request.session.clear()
    request.session.flush()
    return redirect('index')


def home(request):
    user_id = request.session.get('user_id')

    if user_id:
        try:
            # データベースから再度取得
            employee = Employee.objects.get(id=user_id)
            # 必要な情報をテンプレートに渡す
            return render(request, 'business_management/home.html', {'employee': employee})
        except Employee.DoesNotExist:
            messages.error(request, 'Employee not found')
            return redirect('index')
    return redirect('index')

