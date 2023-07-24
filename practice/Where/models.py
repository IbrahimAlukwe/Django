from django.db import models

# Create your models here.

# class is just a layout or blueprint on how something is support to appper
# modules stores data from database
# the name students represent the table

class students(models.Model):
    name = models.CharField(max_length=22,blank=False,null=False)
    school = models.CharField(max_length=45,blank=False, null=False)
    email = models.EmailField()

def __str__(self):
      return self.name

# any time you modify models file you must make and run migrations

