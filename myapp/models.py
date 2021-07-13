from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    count = models.PositiveIntegerField()


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateField()