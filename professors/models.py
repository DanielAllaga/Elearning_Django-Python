from django.db import models
import uuid 

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    #to see customer name in admin panel instead of object
    def __str__(self):
        return self.name

#creating class
class Class(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    class_code = models.CharField(max_length=200, null=True)
    class_description = models.CharField(max_length=200, null=True)
    class_section = models.CharField(max_length=200, null=True)
    unique_code = models.CharField(max_length=200, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.class_code
