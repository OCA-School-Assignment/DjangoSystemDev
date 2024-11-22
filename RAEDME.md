### check if models connect db
```
from business_management
.models import Department, Employee

# Departmentデータ確認
departments = Department.objects.all()
for dept in departments:
    print(dept.name)

# Employeeデータ確認
employees = Employee.objects.all()
for emp in employees:
    print(emp.id, emp.name, emp.department.name, emp.email)

```