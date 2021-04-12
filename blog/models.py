from django.db import models

# Create your models here.


class Author(models.Model):
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)


class Publication(models.Model):
    title = models.CharField(max_length=200)
    preview_description = models.TextField()
    description = models.TextField()
    external_article = models.TextField()
    image = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
