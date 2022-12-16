from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
import uuid

# Create your models here.

class author(models.Model):
    authorId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30, null=True, blank=True)

     # returns the state of the object name to be displayed
    def __str__(self) -> str:
        return self.name

class publisher(models.Model):
    publisherId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

     # returns the state of the object name to be displayed
    def __str__(self) -> str:
        return self.name

class book(models.Model):
    bookId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(max_length=300, unique=True)
    author = models.CharField(max_length=300)
    publisher = models.CharField(max_length=300)
    rating = models.IntegerField(default=1 , validators=[MaxValueValidator(5), MinValueValidator(1)])
    price = models.BigIntegerField(default=400, null=True, blank=True)

     # returns the state of the object name to be displayed
    def __str__(self) -> str:
        return self.title
