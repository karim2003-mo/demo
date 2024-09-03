from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save ,pre_save,post_delete
class Team(models.Model) :
    name = models.CharField(max_length=30,null=True,blank=True)
    founded_at = models.DateField(null=True,blank=True)
    logo = models.TextField(null=True,blank=True)
    coach = models.CharField(max_length=30,null=True,blank=True)
    leagues = models.IntegerField(null=True,blank=True)
    local_cup= models.IntegerField(null=True,blank=True)
    local_super = models.IntegerField(null=True,blank=True)
    continental_cups = models.CharField(max_length=30,null=True,blank=True)
    squad=models.JSONField(default={"squad" : []})
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
    number=models.IntegerField(blank=True,null=True)
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
    current_value=models.IntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name
@receiver(pre_save,sender=player)
def transefer_player(sender,instance,**kwargs) :
    try :
        if sender.team != instance.team and sender.team != None:    
            team=Team.objects.get(name=sender.team)
            team.squad["squad"].remove([instance.id,instance.name])
            team.save()
        if sender.team == None :
            team=Team.objects.get(name=instance.team)
            team.squad["squad"].append([instance.id,instance.name])
        if sender.name != instance.name :
            team=Team.objects.get(name=instance.team)
            team.squad["squad"].remove([sender.id,sender.name])
    except :
        pass
@receiver(post_save,sender=player)
def add_playrt_to_squad(sender,instance,created,**kwargs) :
    if instance.team !=None :
        team=Team.objects.get(name=instance.team)
        team.squad["squad"].append([instance.id,instance.name])
        team.save()
@receiver(post_delete,sender=player)
def delete_playrt_from_squad(sender,instance,**kwargs) :
        team=Team.objects.get(name=instance.team)
        team.squad["squad"].remove([instance.id,instance.name])
        team.save()