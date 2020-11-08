from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class People(models.Model):

    id = models.CharField(primary_key=True,max_length=300, unique=True, null=False)
    name = models.CharField(max_length=300,  null=False)
    gender = models.CharField(max_length=300,  null=False)
    age = models.CharField(max_length=300,  null=False)
    eye_color = models.CharField(max_length=300,  null=False)
    hair_color =  models.CharField(max_length=300,  null=False)
   

    def __str__(self):
        return str(self.name)
