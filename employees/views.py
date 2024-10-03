from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees, Salaries

def employee_by_telegram_id(request, telegram_id):
    try:
        employee = Employees.objects.get(telegram_id=telegram_id)
        salary = Salaries.objects.filter(employee=employee).first()
        total_salary = salary.base_salary + salary.bonuses + salary.overtime_pay

        return render(request, 'employees/employee_detail.html', {
            'employee': employee,
            'salary': salary,
            'total_salary': total_salary
        })
    except Employees.DoesNotExist:
        return HttpResponse("Employee not found.", status=404)
