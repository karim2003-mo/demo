from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model) :
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    score=models.IntegerField(null=True,blank=True)
    favourite_club=models.CharField(null=True,blank=True)
# Create your models here.
