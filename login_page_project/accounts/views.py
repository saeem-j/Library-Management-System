from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return redirect("login")


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password:
            return render(request, "signup.html", {
                "error": "Please fill all required fields."
            })

        if password != confirm_password:
            return render(request, "signup.html", {
                "error": "Passwords do not match."
            })

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {
                "error": "Username already exists."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {
                "error": "Email already exists."
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        return redirect("login")

    return render(request, "signup.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(request, "login.html", {
            "error": "Invalid username or password."
        })

    return render(request, "login.html")


@login_required
def home(request):
    return render(request, "home.html")


def user_logout(request):
    logout(request)
    return redirect("login")
