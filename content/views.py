from django.shortcuts import render,get_list_or_404
import json
from .models import *
from django.http import HttpResponse, JsonResponse
def getchamp(text)-> list :
    l=[]
    my_text=str(text)
    a=my_text.split(',')[0]
    my_text= my_text.removeprefix(f"{a},")
    l.append(int(a))
    b=my_text.split(',')[0]
    my_text= my_text.removeprefix(f"{b},")
    l.append(int(b))
    l.append(int(my_text))
    return l
def all_teams(request) :
    teams=Team.objects.all()
    l=[]
    for team in teams :
        champions= getchamp(team.continental_cups)
        mp={
            "id" : team.pk ,
            "name" :team.name ,
            "founded at" : team.founded_at ,
            "logo" : team.logo ,
            "leagues" : team.leagues ,
            "cups" : team.local_cup ,
            "super" : team.local_super ,
            "africia leagues" : champions[0],
            "africia confedration" : champions[1],
            "africia super" : champions[2],
            "coach" : team.coach,
            "squad" : team.squad,
        }
        l.append(mp)
    print(l)
    return JsonResponse({"result" : l}) 
def view_player(request,team,) :
    obj=Team.objects.get(name=team).squad["squad"]
    l=[]
    for i in obj:
        pl=player.objects.get(pk=i[0])
        birth=str(pl.birht_date).strip()
        print(pl.birht_date)
        age=2024-int(birth)
        curr=0
        if pl.current_value != None :
            if int(pl.current_value) <=1000 :
                curr=f"{pl.current_value}k $"
            else :
                curr=f"{float(pl.current_value/1000)}m $"
        dat= {
            'id':pl.pk,
            'name' :pl.name,
            'number':pl.number,
            'image':pl.image,
            'team':pl.team.name,
            'age':age,
            'current value':curr,
            "goals" :pl.goals,
            "assists" : pl.assist,
            "yellow card" :pl.yellow_card,
            "red card" : pl.red_card,
        }
        l.append(dat)
    return JsonResponse({"result" : l})
# Create your views here.
