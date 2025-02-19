from django.db import models
from .forms import ContactForm

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    def __str__(self): # this is a string representation of the object, for calling the class
        return self.name