# Generated by Django 3.2.7 on 2021-11-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Mobile_no',
            field=models.CharField(max_length=10),
        ),
    ]
