from django.contrib import admin
from .models import Employees, Salaries, Position

admin.site.register(Employees)
admin.site.register(Salaries)
admin.site.register(Position)
