from django.db import models

# Create your models here.

class Item(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    published=models.DateField()
    isbn=models.CharField(max_length=20)
    summary=models.TextField()

def __self__(self):
    return self.title