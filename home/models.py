import email
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
# Modal- is a way to tell django i want to create the database

class Contact(models.Model):
    # to keep the data persistent in the DB coming from contact.html
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone=models.CharField(max_length=10)
    desc=models.TextField()   #for storing the lage text in DB in Django

    def __str__(self):
        return self.name+'--'+ self.email


