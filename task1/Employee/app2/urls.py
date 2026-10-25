from django.urls import path

from .views import (
    display,
    addEmpData,
    employee_detail,
    updateEmpData,
    deleteEmpData,
    contact,
    about
)


urlpatterns = [

    # Employee list
    path(
        'empdata/',
        display,
        name='empdata'
    ),

    # Add employee
    path(
        'addemp/',
        addEmpData,
        name='addemp'
    ),

    # Employee details
    path(
        'employee/<int:id>/',
        employee_detail,
        name='employee_detail'
    ),

    # Update employee
    path(
        'employee/<int:id>/update/',
        updateEmpData,
        name='update_employee'
    ),

    # Delete employee
    path(
        'employee/<int:id>/delete/',
        deleteEmpData,
        name='delete_employee'
    ),
    path(
        'contact/',
        contact,
        name='contact'
    ),
    path(
        'about/',
        about,
        name='about'
    )
]