from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model) :
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    score=models.JSONField(default={"score":[]})
    favourite_club=models.CharField(null=True,blank=True)
    leagues=models.JSONField(default={"leagues":[]})
    squad=models.JSONField(default={"squad":[]})
    squad_name=models.CharField(null=True,blank=True)
# Create your models here.
