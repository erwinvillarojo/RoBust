# Generated by Django 3.1.1 on 2020-12-04 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robust', '0002_auto_20201204_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='imagesBus/'),
        ),
    ]