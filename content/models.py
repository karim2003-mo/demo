from django.db import models
class Team(models.Model) :
    name = models.CharField(max_length=30,null=True,blank=True)
    founded_at = models.DateField(null=True,blank=True)
    logo = models.TextField(null=True,blank=True)
    coach = models.CharField(max_length=30,null=True,blank=True)
    leagues = models.IntegerField(null=True,blank=True)
    local_cup= models.IntegerField(null=True,blank=True)
    local_super = models.IntegerField(null=True,blank=True)
    continental_cups = models.CharField(max_length=30,null=True,blank=True)
    squad=models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name
class player(models.Model) :
    x=[
    ("Gk","Gk"),
    ("Lb","Lb"),
    ("cb","cb"),
    ("Rb","Rb"),
    ("Dmf","Dmf"),
    ("Cmf","Cmf"),
    ("Amf","Amf"),
    ("Lwf","Lwf"),
    ("Rwf","Rwf"),
    ("Ss","Ss"),
    ("Cf","Cf"),
    ]
    name=models.CharField(max_length=30,null=True,blank=True)
    birht_date=models.CharField(max_length=30,null=True,blank=True)
    image=models.TextField(null=True,blank=True)
    team=models.ForeignKey(Team,null=True,blank=True,on_delete=models.PROTECT)
    nationality=models.CharField(max_length=30,null=True,blank=True)
    position=models.CharField(max_length=30,null=True, blank=True,choices=x)
    goals = models.IntegerField(null=True,blank=True)
    assist = models.IntegerField(null=True,blank=True)
    clean_sheet = models.IntegerField(null=True,blank=True)
    yellow_card= models.IntegerField(null=True,blank=True)
    red_card = models.IntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name