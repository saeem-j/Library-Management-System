from django.shortcuts import render
def courses(request):
        percentage=78
        if percentage>=85:
            eligible_courses=["B.Tech CSE","B.Tech AI & DS","B.Tech ECE"]
        elif percentage>=70:
            eligible_courses=["B.Tech AI & DS","B.Tech ECE"]
        elif percentage>=60:
            eligible_courses=["B.Tech ECE"]
        else:
            eligible_courses=["No course available"]
        return render(request,"courses.html",{"percentage":percentage,"eligible_courses":eligible_courses})
