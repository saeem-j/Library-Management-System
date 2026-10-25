from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignupForm, LoginForm, BookIssueForm
from .models import BookIssue

def home(request):
    return render(request, "home.html")

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["name"]
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=name
        )
        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("dashboard")

    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        form.add_error(None, "Invalid username or password.")

    return render(request, "login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    total_books = BookIssue.objects.count()
    return render(request, "dashboard.html", {"total_books": total_books})

@login_required
def issue_book(request):
    form = BookIssueForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        book = form.save()
        return redirect("success", book_id=book.id)

    return render(request, "issue_book.html", {"form": form})

@login_required
def success_page(request, book_id):
    book = get_object_or_404(BookIssue, id=book_id)
    return render(request, "success.html", {"book": book})

@login_required
def view_books(request):
    books = BookIssue.objects.all().order_by("-issue_date", "-id")
    return render(request, "view_books.html", {"books": books})

 
@login_required
def delete_book(request, book_id):
    book = BookIssue.objects.filter(id=book_id).first()
    if book is None:
        messages.error(request, "That book record no longer exists. Please choose a book from the list.")
        return redirect("view_books")

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect("view_books")

    return render(request, "delete_book.html", {"book": book})

def update_book(request, book_id):
    book = get_object_or_404(BookIssue, id=book_id)
    form = BookIssueForm(request.POST or None, instance=book)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Book updated successfully.")
        return redirect("view_books")
    return render(request, "update_book.html", {"form": form, "book": book})
