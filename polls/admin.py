from django.contrib import admin

from .models import Qualification,Qualification1,Qualification2,Qualification3


# Register your models here.
admin.site.register( Qualification)
admin.site.register( Qualification1)
admin.site.register( Qualification2)
admin.site.register( Qualification3)

class  QualificationModelAdmin(admin.ModelAdmin):
    list_display=['id','Qualification','University','Institution','Year_of_passing','Percentag']

class  QualificationModelAdmin1(admin.ModelAdmin):
    list_display=['id','Qualification1','University1','Institution1','Year_of_passing1','Percentag1']

class  QualificationModelAdmin2(admin.ModelAdmin):
    list_display=['id','Qualification2','University2','Institution2','Year_of_passing2','Percentag2']

class  QualificationModelAdmin3(admin.ModelAdmin):
    list_display=['id','Qualification3','University3','Institution3','Year_of_passing3','Percentag3']