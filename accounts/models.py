from django.db import models
from django.contrib.auth.models import User
from content.models import *
class Profile(models.Model) :
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    is_email_verified=models.BooleanField(default=False)
    score=models.JSONField(default={"score":[0]})
    favourite_club=models.CharField(null=True,blank=True)
    leagues=models.JSONField(default={"leagues":[]})
    squad=models.JSONField(default={"squad":[]})
    substitution=models.JSONField(default={"subs":[]})
    round_stataics=models.JSONField(default={"statics":[]})
    squad_name=models.CharField(null=True,blank=True)
    current_balance=models.FloatField(default=12)
    wildcard=models.BooleanField(default=True)
    freehit=models.BooleanField(default=True)
    tripplecaptin=models.BooleanField(default=True)
    benchboast=models.BooleanField(default=True)
    availiable_tarnsefere=models.IntegerField(default=35)
    captin=models.IntegerField(null=True,blank=True)
    vice=models.IntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.user.username