from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.name