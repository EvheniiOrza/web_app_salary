from rest_framework import viewsets
from .models import Position, Employee, WorkTime, PayrollPeriod, Salary, Deduction
from .serializers import (
    PositionSerializer,
    EmployeeSerializer,
    WorkTimeSerializer,
    PayrollPeriodSerializer,
    SalarySerializer,
    DeductionSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def employee_by_telegram_id(request, telegram_id):
    employee = get_object_or_404(Employee, telegram_id=telegram_id)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer

class PayrollPeriodViewSet(viewsets.ModelViewSet):
    queryset = PayrollPeriod.objects.all()
    serializer_class = PayrollPeriodSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

class DeductionViewSet(viewsets.ModelViewSet):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

    @action(detail=False, methods=['get'])
    def report(self, request):
        aggregated_data = Salary.objects.aggregate(
            total_base_salary=Sum('base_salary'),
            total_overtime_pay=Sum('overtime_pay'),
            total_bonuses=Sum('bonuses'),
        )
        return Response(aggregated_data)