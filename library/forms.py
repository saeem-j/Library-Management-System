from django import forms
from django.contrib.auth.models import User
from .models import BookIssue

class SignupForm(forms.Form):
    name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = [
            "book_id", "book_name", "book_number",
            "student_name", "issue_date", "due_date"
        ]
        widgets = {
            "issue_date": forms.DateInput(attrs={"type": "date"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
