# Generated by Django 3.1.1 on 2020-12-12 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('busID', models.AutoField(primary_key=True, serialize=False)),
                ('busName', models.CharField(max_length=50)),
                ('plateNumber', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('totalSeats', models.PositiveSmallIntegerField(default=51)),
                ('busFare', models.PositiveSmallIntegerField(default=0)),
                ('departureTime', models.TimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(blank=True, null=True, upload_to='imagesBus/')),
            ],
            options={
                'db_table': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='EWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availableBalance', models.IntegerField(default=0)),
                ('currentCashIn', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'EWallet',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePicture', models.ImageField(blank=True, null=True, upload_to='imagesDriver/')),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('emailAddress', models.CharField(max_length=50)),
                ('contactNumber', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('userLogIn', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Driver',
            },
        ),
        migrations.CreateModel(
            name='DashboardUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalUsers', models.IntegerField()),
                ('userLogIn', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'DashboardUser',
            },
        ),
        migrations.CreateModel(
            name='DashboardBus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalBuses', models.IntegerField()),
                ('userLogIn', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'DashboardBus',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('date_booked', models.DateField(auto_now_add=True)),
                ('booking', models.AutoField(primary_key=True, serialize=False)),
                ('seatNumber', models.CharField(max_length=15)),
                ('dateReservation', models.DateField(default=None)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robust.bus')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
    ]
