from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import Employee

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            password = form.cleaned_data['password']
            # カスタム認証ロジック
            try:
                user = Employee.objects.get(email=employee_id, password=password)
                # ログイン成功処理
                messages.success(request, f'Welcome {user.name}')
                return redirect('index')  # ログイン成功後のリダイレクト
            except Employee.DoesNotExist:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Form data is invalid')
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

# def index(request):
#     if request.method == 'POST':
#         return render(request, 'business_management/home.html')
#     print('index')
#     print(request)
#     return render(request, 'business_management/home.html')
