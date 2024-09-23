from django.db import models

# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=5000)
    author = models.TextField(max_length=50)
    date = models.TextField(max_length=20)