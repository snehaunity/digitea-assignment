from django.db import models

# Create your models here.
class Books(models.Model):
   Title=models.CharField(max_length=100,null=True,blank=True) 
   Author=models.CharField(max_length=100,null=True,blank=True)
   Publicationyear=models.IntegerField(null=True,blank=True)


   def __str__(self) -> str:
      return f"{self.Title}"