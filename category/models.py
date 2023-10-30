from django.db import models
from django.shortcuts import reverse,redirect

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.CharField(max_length=200,blank=True,null=True)
    image=models.ImageField(upload_to='store/images',max_length=200,null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)



    def __str__(self) :
        return f'{self.name}'
    


# Create your models here.
