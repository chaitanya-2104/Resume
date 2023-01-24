# Generated by Django 3.2.7 on 2021-12-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20211211_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualification', models.CharField(max_length=100)),
                ('University', models.CharField(max_length=100)),
                ('Institution', models.CharField(max_length=100)),
                ('Year_of_passing', models.PositiveIntegerField()),
                ('Percentag', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Qualification4',
        ),
    ]
