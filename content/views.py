from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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
    return JsonResponse({"result" : l}) 
def view_player(request,team,) :
    obj=Team.objects.get(name=team).squad["squad"]
    l=[]
    for i in obj:
        pl=Player.objects.get(pk=i[0])
        birth=str(pl.birht_date).strip()
        age=2024-int(birth)
        curr=0
        if pl.current_value != None :
            if int(pl.current_value) <=1000 :
                curr=f"{pl.current_value}k $"
            else :
                curr=f"{float(pl.current_value/1000)}m $"
        team_name=""
        if pl.team !=None :
            team_name=pl.team.name
        dat= {
            'id':pl.pk,
            'name' :pl.name,
            'number':pl.number,
            'image':pl.image,
            'team':team_name,
            'possition' :pl.position,
            'nationality':pl.nationality,
            'age':age,
            'current value':curr,
            "goals" :pl.goals,
            "assists" : pl.assist,
            "yellow card" :pl.yellow_card,
            "red card" : pl.red_card,
            "clean sheet":pl.clean_sheet,
        }
        l.append(dat)
    return JsonResponse({"result" : l})
def Gk(request) :
    l=[]
    jsonlist=[]
    all_players=list(Player.objects.all())
    for i in all_players :
        if i.position=="Gk" :
            l.append(Player.objects.get(pk=i.pk))
    print(l)
    for pl in l :
        birth=str(pl.birht_date).strip()
        age=2024-int(birth)
        if pl.current_value != None :
            if int(pl.current_value) <1000 :
                curr=f"{pl.current_value}k $"
            else :
                curr=f"{float(pl.current_value/1000)}m $"
        team_name=""
        if pl.team !=None :
            team_name=pl.team.name
        dat= {
            'id':pl.pk,
            'name' :pl.name,
            'number':pl.number,
            'image':pl.image,
            'team':team_name,
            'possition' :pl.position,
            'nationality':pl.nationality,
            'age':age,
            'current value':curr,
            "goals" :pl.goals,
            "assists" : pl.assist,
            "yellow card" :pl.yellow_card,
            "red card" : pl.red_card,
            "clean sheet":pl.clean_sheet,
        }
        jsonlist.append(dat)
    return JsonResponse({"result":jsonlist})
def Cb(request) :
    l=[]
    jsonlist=[]
    all_players=list(Player.objects.all())
    for i in all_players :
        if i.position=="cb" or i.position=="Lb"or i.position=="Rb"  :
            l.append(Player.objects.get(pk=i.pk))
    print(l)
    for pl in l :
        birth=str(pl.birht_date).strip()
        age=2024-int(birth)
        if pl.current_value != None :
            if int(pl.current_value) <1000 :
                curr=f"{pl.current_value}k $"
            else :
                curr=f"{float(pl.current_value/1000)}m $"
        team_name=""
        if pl.team !=None :
            team_name=pl.team.name
        dat= {
            'id':pl.pk,
            'name' :pl.name,
            'number':pl.number,
            'image':pl.image,
            'team':team_name,
            'possition' :pl.position,
            'nationality':pl.nationality,
            'age':age,
            'current value':curr,
            "goals" :pl.goals,
            "assists" : pl.assist,
            "yellow card" :pl.yellow_card,
            "red card" : pl.red_card,
            "clean sheet":pl.clean_sheet,
        }
        jsonlist.append(dat)
    return JsonResponse({"result":jsonlist})
def Cmf(request) :
    l=[]
    jsonlist=[]
    all_players=list(Player.objects.all())
    for i in all_players :
        if i.position=="Dmf" or i.position=="Cmf"or i.position=="Amf"or i.position=="Rwf"or i.position=="Lwf"  :
            l.append(Player.objects.get(pk=i.pk))
    print(l)
    for pl in l :
        birth=str(pl.birht_date).strip()
        age=2024-int(birth)
        if pl.current_value != None :
            if int(pl.current_value) <1000 :
                curr=f"{pl.current_value}k $"
            else :
                curr=f"{float(pl.current_value/1000)}m $"
        team_name=""
        if pl.team !=None :
            team_name=pl.team.name
        dat= {
            'id':pl.pk,
            'name' :pl.name,
            'number':pl.number,
            'image':pl.image,
            'team':team_name,
            'possition' :pl.position,
            'nationality':pl.nationality,
            'age':age,
            'current value':curr,
            "goals" :pl.goals,
            "assists" : pl.assist,
            "yellow card" :pl.yellow_card,
            "red card" : pl.red_card,
            "clean sheet":pl.clean_sheet,
        }
        jsonlist.append(dat)
    return JsonResponse({"result":jsonlist})
def Cf(request) :
    l=[]
    jsonlist=[]
    all_players=list(Player.objects.all())
    for i in all_players :
        if i.position=="Cf" or i.position=="Ss"  :
            l.append(Player.objects.get(pk=i.pk))
    print(l)
    for pl in l :
        birth=str(pl.birht_date).strip()
        age=2024-int(birth)
        if pl.current_value != None :
            if int(pl.current_value) <1000 :
                curr=f"{pl.current_value}k $"
            else :
                curr=f"{float(pl.current_value/1000)}m $"
        team_name=""
        if pl.team !=None :
            team_name=pl.team.name
        dat= {
            'id':pl.pk,
            'name' :pl.name,
            'number':pl.number,
            'image':pl.image,
            'team':team_name,
            'possition' :pl.position,
            'nationality':pl.nationality,
            'age':age,
            'current value':curr,
            "goals" :pl.goals,
            "assists" : pl.assist,
            "yellow card" :pl.yellow_card,
            "red card" : pl.red_card,
            "clean sheet":pl.clean_sheet,
        }
        jsonlist.append(dat)
    return JsonResponse({"result":jsonlist})
csrf_exempt
def getsquad(request):
    if request.methos=='POST' :
        l=[]
        data=json.loads(request.body)
        list=data['list']
        for i in list :
            pl=Player.objects.get(pk=i)
            birth=str(pl.birht_date).strip()
            age=2024-int(birth)
            if pl.current_value != None :
                if int(pl.current_value) <1000 :
                    curr=f"{pl.current_value}k $"
                else :
                    curr=f"{float(pl.current_value/1000)}m $"
            team_name=""
            if pl.team !=None :
                team_name=pl.team.name
            dat= {
            'id':pl.pk,
            'name' :pl.name,
            'number':pl.number,
            'image':pl.image,
            'team':team_name,
            'possition' :pl.position,
            'nationality':pl.nationality,
            'age':age,
            'current value':curr,
            "goals" :pl.goals,
            "assists" : pl.assist,
            "yellow card" :pl.yellow_card,
            "red card" : pl.red_card,
            "clean sheet":pl.clean_sheet,
            }
            l.append(dat)
        return JsonResponse({"result":dat})
    else :
        return JsonResponse({"result":"fail"})
# Create your views here.
