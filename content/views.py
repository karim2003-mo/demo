from django.shortcuts import render
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
# Create your views here.
