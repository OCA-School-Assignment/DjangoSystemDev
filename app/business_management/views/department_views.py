from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from ..models import Department
from ..forms import DepartmentRegisterForm


def department_management(request):
    return render(request, 'business_management/EmployeeManagementSystem/DepartmentManagement/selection.html')


class DepartmentListView(ListView):
    model = Department
    template_name =  'business_management/EmployeeManagementSystem/DepartmentManagement/department_management.html'
    context_object_name = 'departments'


def department_register(request):
    if request.method == 'POST':
        form = DepartmentRegisterForm(request.POST)
        if form.is_valid():
            department = form.save()
            messages.success(request, f'部署ID:「{department.id}」、部署名「{department.name}」を登録しました。')
            return redirect('department-manage')
        else:
            messages.error(request, '部署IDまたは部署名が既に登録されています。')
            return redirect('department-manage')
    else:
        form = DepartmentRegisterForm()
    return render(request, 'business_management/EmployeeManagementSystem/DepartmentManagement/department_register.html', {'form': form})


def department_edit(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    params = {
        'form': DepartmentRegisterForm(instance=department),
        'department': department,
    }
    if request.method == 'POST':
        form = DepartmentRegisterForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, f'部署ID:「{department.id}」、部署名:「{department.name}」を更新しました。')
            return redirect('department-manage')
    return render(request, 'business_management/EmployeeManagementSystem/DepartmentManagement/department_edit.html', params)


def department_delete(request, department_id):
    if request.method == 'POST':
        department = get_object_or_404(Department, id=department_id)
        deleted_department_id = department.id
        deleted_department_name = department.name
        department.delete()
        messages.error(request, f'部署ID:「{deleted_department_id}」、部署名:「{deleted_department_name}」を削除しました。')
        return redirect('department-manage')
    return redirect('department-manage')