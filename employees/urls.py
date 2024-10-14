from django.urls import path
from . import views

urlpatterns = [
    path('employee/telegram/<str:telegram_id>/', views.employee_by_telegram_id, name='employee_by_telegram_id'),
]
