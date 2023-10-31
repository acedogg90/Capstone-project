# Generated by Django 4.2.6 on 2023-10-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("no_of_guests", models.PositiveIntegerField()),
                ("booking_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("inventory", models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Restaurant",
        ),
    ]
