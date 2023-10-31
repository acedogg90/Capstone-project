from django.db import models

# Create your models here.

class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # This is automatically created by Django, but included for clarity
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)  # This is automatically created by Django, but included for clarity
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}' # A  method that returns a string representation of the model instance.
