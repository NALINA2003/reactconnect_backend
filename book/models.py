from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length = 100)
    author_name = models.CharField(max_length=100)
    general = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.BigIntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name