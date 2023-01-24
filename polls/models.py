from django.db import models

# Create your models here.
class  Qualification(models.Model):
    Qualification=models.CharField(max_length=100)
    University=models.CharField(max_length=100)
    Institution=models.CharField(max_length=100)
    Year_of_passing=models.PositiveIntegerField()
    Percentag=models.CharField(max_length=100)

class  Qualification1(models.Model):
    Qualification1=models.CharField(max_length=100)
    University1=models.CharField(max_length=100)
    Institution1=models.CharField(max_length=100)
    Year_of_passing1=models.PositiveIntegerField()
    Percentag1=models.CharField(max_length=100)

class  Qualification2(models.Model):
    Qualification2=models.CharField(max_length=100)
    University2=models.CharField(max_length=100)
    Institution2=models.CharField(max_length=100)
    Year_of_passing2=models.PositiveIntegerField()
    Percentag2=models.CharField(max_length=100)

class  Qualification3(models.Model):
    Qualification3=models.CharField(max_length=100)
    University3=models.CharField(max_length=100)
    Institution3=models.CharField(max_length=100)
    Year_of_passing3=models.PositiveIntegerField()
    Percentag3=models.CharField(max_length=100)
