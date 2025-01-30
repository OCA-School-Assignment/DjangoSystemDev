from ..models import Employee
from ..forms import EmployeeSearchForm, EmployeeRegisterForm, EmployeeEditForm
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.utils import IntegrityError


def employee_management(request):
    return render(request, 'business_management/EmployeeManagementSystem/EmployeeManagement/selection.html')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'business_management/EmployeeManagementSystem/EmployeeManagement/employee_management.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = EmployeeSearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_type = self.request.GET.get('search_type', '')
        query = self.request.GET.get('query', '')
        
        if search_type == 'id' and query:
            # queryset = queryset.filter(id=query)
            queryset = queryset.filter(id__icontains=query)
        elif search_type == 'name' and query:
            queryset = queryset.filter(name__icontains=query)
        
        return queryset


def employee_register(request):    
    params = {
        'form': EmployeeRegisterForm()
    }
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            name = form.cleaned_data['name']
            department_obj = form.cleaned_data['department_id']
            department_id = department_obj.id if department_obj else None
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                employee = Employee.objects.create(id=employee_id, name=name, department_id=department_id, email=email, password=password)
                employee.save()
                messages.success(request, f'従業員ID:「{employee.id}」、従業員名:「{employee.name}」を登録しました。')
                return redirect('/employee-management/register')
            except IntegrityError:
                messages.error(request, '従業員IDまたはメールアドレスが既に登録されています。')
                return redirect('/employee-management/register')
    return render(request, 'business_management/EmployeeManagementSystem/EmployeeManagement/employee_register.html', params)


def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    params = {
        'form': EmployeeEditForm(instance=employee),
        'employee': employee,
    }
    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'従業員ID:「{employee.id}」、従業員名:「{employee.name}」を更新しました。')
            return redirect('employee-manage')
    return render(request, 'business_management/EmployeeManagementSystem/EmployeeManagement/employee_edit.html', params)


def employee_delete(request, employee_id):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, id=employee_id)
        deleted_employee_id = employee.id
        deleted_employee_name = employee.name
        employee.delete()
        messages.error(request, f'従業員ID:「{deleted_employee_id}」、従業員名:「{deleted_employee_name}」を削除しました。')
        return redirect('employee-manage')
    return redirect('employee-manage')
