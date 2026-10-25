# from django.contrib import admin

# # Register your models here.
# from .models import Department, Employee, Company

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display= ('id','name','email','age','salary','address','company', 'department')
#     search_fields=('name','email')
#     ordering = ('id',)
#     list_filter = ('company',)
    
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display= ('id','name','email','branchNumber','location',)
    
#     search_fields=('name','email')
#     ordering = ('id',)  
    
# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display= ('id','name','phone',)

from django.contrib import admin
from .models import Employee, Company, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'age',
        'salary',
        'department',
        'company',
        'address',
    )

    search_fields = (
        'name',
        'email',
    )

    list_filter = (
        'department',
        'company',
    )

    ordering = (
        'id',
    )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'branchNumber',
        'location',
    )

    search_fields = (
        'name',
        'email',
        'branchNumber',
    )

    ordering = (
        'id',
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'phone',
    )

    search_fields = (
        'name',
        'phone',
    )

    ordering = (
        'id',
    )