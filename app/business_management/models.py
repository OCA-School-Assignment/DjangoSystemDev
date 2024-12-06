from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name
