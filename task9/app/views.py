from django.shortcuts import render
def loan(request):
    age=25
    salary=40000
    credit_score=750
    if age>=21 and salary>=30000 and credit_score>=700:
        result="Loan Eligible"
    elif age>=21 and salary>=30000:
        result="Eligible, but credit score is low"
    elif age<21:
        result="Not Eligible: Age must be 21 or above"
    else:
        result="Not Eligible: Salary is too low"
    return render(request,"loan.html",{"age":age,"salary":salary,"credit_score":credit_score,"result":result})
