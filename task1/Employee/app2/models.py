from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    branchNumber = models.CharField(max_length=10, unique=True)
    location = models.TextField(max_length=200, default='Null')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    salary = models.FloatField()
    address = models.TextField(max_length=200, default='Null')

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True,
        blank=True
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name