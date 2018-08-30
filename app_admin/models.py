from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)




    def __str__(self):
        return self.title