# Generated by Django 3.1.1 on 2020-11-25 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0004_auto_20201125_1046'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buses',
            new_name='Bus',
        ),
        migrations.AlterModelTable(
            name='bus',
            table='Bus',
        ),
    ]
