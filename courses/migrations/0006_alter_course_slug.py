# Generated by Django 3.2.5 on 2021-07-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210716_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
