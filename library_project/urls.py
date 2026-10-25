from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("issue-book/", views.issue_book, name="issue_book"),
    path("success/<int:book_id>/", views.success_page, name="success"),
    path("books/", views.view_books, name="view_books"),    
    path("delete-book/<int:book_id>/", views.delete_book, name="delete_book"),
    path("update-book/<int:book_id>/", views.update_book, name="update_book"),
    
]
    