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
class Player(models.Model) :
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
    image=models.TextField(default="https://raw.githubusercontent.com/karim2003-mo/football-images/master/players/")
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
        return f'{self.name} ==============> {self.team.name}'
    class Meta :
        ordering=['team','name']
@receiver(pre_save,sender=Player)
def transefer_player(sender,instance,**kwargs) :
    
    
    
    
    try :
        print("==============================")
        if sender.objects.get(pk=instance.pk).team != instance.team:
            if sender.objects.get(pk=instance.pk).team != None and instance.team != None :
                old_team=Team.objects.get(name=sender.objects.get(pk=instance.pk).team)
                new_team=Team.objects.get(name=instance.team)
                old_team.squad["squad"].remove([instance.id,instance.name])
                new_team.squad["squad"].append([instance.id,instance.name])
                new_team.save()
                old_team.save()
                print("==============================")
            else :
                if sender.objects.get(pk=instance.pk).team == None :
                    new_team=Team.objects.get(name=instance.team)
                    new_team.squad["squad"].append([instance.id,instance.name])
                    new_team.save()
                elif instance.team == None :
                    old_team=Team.objects.get(name=sender.objects.get(pk=instance.pk).team)
                    old_team.squad["squad"].remove([instance.id,instance.name])
                    old_team.save()
    except :
        pass
@receiver(post_save,sender=Player)
def add_playrt_to_squad(sender,instance,created,**kwargs) :
    if created and instance.team !=None :
        team=Team.objects.get(name=instance.team)
        if [instance.id,instance.name] not in team.squad["squad"]:
                team.squad["squad"].append([instance.id,instance.name])
        if [instance.id,instance.name] not in team.squad["squad"]:
                team.squad["squad"].append([instance.id,instance.name])
        team.save()
@receiver(post_delete,sender=Player)
def delete_playrt_from_squad(sender,instance,**kwargs) :
    if instance.team != None:
        team=Team.objects.get(name=instance.team)
        team.squad["squad"].remove([instance.id,instance.name])
        team.save()