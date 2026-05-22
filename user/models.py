from django.db import models

# Create your models here.
class Users(models.Model):
     name = models.CharField(max_length = 100)
     age = models.IntegerField()
     email = models.EmailField()
     phone_number = models.CharField(max_length = 11)
     password = models.CharField()
     
     def __str__(self):
          return self.name

