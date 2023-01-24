from django.db import models




# Create your models here.
class Forms(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    Mobile_no=models.IntegerField(blank=True)
    Email=models.EmailField()
    Age=models.PositiveIntegerField()
    Education=models.CharField(max_length=100)
    Upload_Documents=models.FileField(upload_to='doc',blank=True)
#upload_to='doc',blank=True