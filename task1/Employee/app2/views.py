from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee, Department, Company



def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def display(request):

    data = Employee.objects.all()

    return render(
        request,
        "empdata.html",
        {
            'employeedata': data
        }
    )


# --------------------------------
# ADD EMPLOYEE
# --------------------------------

def addEmpData(request):

    dep_data = Department.objects.all()
    com_data = Company.objects.all()

    if request.method == "POST":

        name = request.POST.get('nm')
        age = request.POST.get('ag')
        email = request.POST.get('em')
        salary = request.POST.get('sal')
        address = request.POST.get('add')

        department = request.POST.get('dep')
        company = request.POST.get('comp')

        Employee.objects.create(
            name=name,
            age=age,
            email=email,
            salary=salary,
            address=address,
            department_id=department,
            company_id=company
        )

        return redirect('empdata')

    return render(
        request,
        'from.html',
        {
            'dep_data': dep_data,
            'com_data': com_data
        }
    )


# --------------------------------
# EMPLOYEE DETAIL
# --------------------------------

def employee_detail(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    return render(
        request,
        'employee_detail.html',
        {
            'employee': employee
        }
    )


# --------------------------------
# UPDATE EMPLOYEE
# --------------------------------

def updateEmpData(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    dep_data = Department.objects.all()
    com_data = Company.objects.all()

    if request.method == "POST":

        employee.name = request.POST.get('nm')
        employee.age = request.POST.get('ag')
        employee.email = request.POST.get('em')
        employee.salary = request.POST.get('sal')
        employee.address = request.POST.get('add')

        employee.department_id = request.POST.get('dep')
        employee.company_id = request.POST.get('comp')

        employee.save()

        return redirect('empdata')

    return render(
        request,
        'update.html',
        {
            'employee': employee,
            'dep_data': dep_data,
            'com_data': com_data
        }
    )


# --------------------------------
# DELETE EMPLOYEE
# --------------------------------

def deleteEmpData(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    if request.method == "POST":

        employee.delete()

        return redirect('empdata')

    return render(
        request,
        'delete.html',
        {
            'employee': employee
        }
    
    )
    
     