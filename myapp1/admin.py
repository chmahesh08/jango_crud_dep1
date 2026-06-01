from django.contrib import admin

# Register your models here.
from myapp1.models import employee


class employeeAdmin(admin.ModelAdmin):
    list_display = ('Employee_name', 'Employee_id', 'Employee_email', 'Employee_salary')
    ordering = ['Employee_id']

admin.site.register(employee, employeeAdmin)