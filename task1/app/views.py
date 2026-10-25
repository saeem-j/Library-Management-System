from django.shortcuts import render
def result(request):
    student={"name":"Yash","marks":[70,80,65,75,90]}
    total=sum(student["marks"])
    percentage=total/5
    return render(request,"result.html",{"student":student,"total":total,"percentage":percentage})
