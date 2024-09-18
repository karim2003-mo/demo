from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model) :
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    score=models.JSONField(default={"score":[]})
    favourite_club=models.CharField(null=True,blank=True)
    leagues=models.JSONField(default={"leagues":[]})
    squad=models.JSONField(default={"squad":[]})
    squad_name=models.CharField(null=True,blank=True)
    current_balance=models.IntegerField(default=12)
    wildcard=models.BooleanField(default=True)
    freehit=models.BooleanField(default=True)
    tripplecaptin=models.BooleanField(default=True)
    availiable_tarnsefere=models.IntegerField(default=35)
    def __str__(self) -> str:
        return self.user.username
# Create your models here.
