from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='cover')
    genre = models.ManyToManyField(Genre, related_name="books")
    author = models.CharField(max_length=200)
    purchase_link = models.URLField(max_length=500)
    summary = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return f"{self.book_name}"

class Comment(models.Model):
    username = models.CharField(max_length=100, default='User')
    date_posted = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=400)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")

