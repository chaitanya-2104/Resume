# Generated by Django 3.2.7 on 2021-12-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20211211_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='Age',
            field=models.PositiveIntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='forms',
            name='Mobile_no',
            field=models.IntegerField(max_length=10),
        ),
    ]
