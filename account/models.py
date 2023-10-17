from django.db import models

# Create your models here.


class Request(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
