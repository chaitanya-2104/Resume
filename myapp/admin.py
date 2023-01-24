from django.contrib import admin
from .models import Forms


# Register your models here.
admin.site.register(Forms)

class FormModelAdmin(admin.ModelAdmin):
    list_display=['id','Name','Address','Mobile_no','Email','Age','Education','Upload_Documents']