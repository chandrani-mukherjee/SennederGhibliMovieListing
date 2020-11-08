from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from MovieCharacter.models import People
# Create your models here.

class Movie(models.Model):

    id = models.CharField(primary_key=True,max_length=300, unique=True, null=False)
    title = models.CharField(max_length=300,null=False)
    description = models.CharField(max_length=1000, null=False)
    director = models.CharField(max_length=300,  null=False)
    producer = models.CharField(max_length=300,  null=False)
    release_date =  models.CharField(max_length=300,  null=False)
    rt_score = models.IntegerField(default=0, null=False)
    character = models.ManyToManyField(People)

    def __str__(self):
        return str(self.id)
