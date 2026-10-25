from django.db import models

class BookIssue(models.Model):
    book_id = models.CharField(max_length=50)
    book_name = models.CharField(max_length=150)
    book_number = models.CharField(max_length=50)
    student_name = models.CharField(max_length=150)
    issue_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.book_name} - {self.student_name}"
