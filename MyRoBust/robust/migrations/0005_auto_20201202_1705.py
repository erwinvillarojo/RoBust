# Generated by Django 3.1.1 on 2020-12-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robust', '0004_booking_date_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_booked',
            field=models.DateField(auto_now_add=True),
        ),
    ]
