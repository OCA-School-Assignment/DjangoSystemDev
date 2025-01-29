from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

def department_required(view_func, allowed_departments):
    def _wrapped_view(request, *args, **kwargs):
        employee_department = request.session.get('department_name')
        
        if employee_department not in allowed_departments:
            return HttpResponseForbidden("アクセスが許可されていません。")
        return view_func(request, *args, **kwargs)
    return _wrapped_view