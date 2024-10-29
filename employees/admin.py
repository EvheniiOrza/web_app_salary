from django.contrib import admin
from .models import Employee, Salary, Position, PayrollPeriod

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Position)
admin.site.register(PayrollPeriod)