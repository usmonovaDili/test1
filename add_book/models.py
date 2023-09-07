from datetime import datetime

from django.db import models
from book_app.models import CustomUser


class GenerModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    pic = models.ImageField(upload_to="media/")
    email = models.EmailField(max_length=200, unique=True)
    date_of_birth = models.DateField(default=datetime.now)
    genre = models.ForeignKey(GenerModel, on_delete=models.CASCADE)
    country = models.CharField(default='', max_length=25)
    is_dead = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name




class BookModel(models.Model):
    name = models.CharField(default='', max_length=25)
    image = models.ImageField(upload_to='book/')
    price = models.FloatField(default=0)
    pages = models.PositiveSmallIntegerField(default=5)
    year = models.PositiveSmallIntegerField(default=1900)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(GenerModel, on_delete=models.SET_NULL, null=True)
    desc = models.TextField(default='')

    def __str__(self):
        return self.name
