import json
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from content.models import *
def profile_data(request,id) :
    profile=Profile.objects.get(pk=id)
    data={"status" : "succes",
        "userdata" :{
            "id":profile.pk,
            "username" :profile.user.username,
            "squad name" : profile.squad_name,
            "squad":profile.squad["squad"],
            "score" :profile.score["score"],
            "favourite club" :profile.favourite_club,
            "leagues":profile.leagues['leagues'],
            "current_balance":profile.current_balance,
            "wildcard":profile.wildcard,
            "freehit":profile.freehit,
            "tripplecaptain":profile.tripplecaptin,
            "availiable transefere":profile.availiable_tarnsefere,
            "subs" : profile.substitution['subs'],
            "captain":profile.captin,
            "vice":profile.vice,
            "benchboast":profile.benchboast,
            "points":profile.round_stataics
        }
            }
    return JsonResponse({"result":data})
@csrf_exempt
def login(request) :
    if request.method=='POST' :
        try :
            data=json.loads(request.body)
            print(request.body)
            username = data.get('username')
            password = data.get('password')
            user= authenticate(request,username=username, password=password)
            if user is not None :
                print("user found")
                x_user=User.objects.get(username=username)
                profile_data=Profile.objects.get(user=x_user)
                return JsonResponse({"status":"succes",
                                    "id":profile_data.pk})
            else :
                return JsonResponse({"status":"fail",})
        except Exception as e:
            return JsonResponse({"status":"error"})
    else :
        return JsonResponse({"status":"unexcepected request"})
@csrf_exempt
def signup(request) :
    if request.method=='POST' :
        try :
            data = json.loads(request.body)
            username = data.get('username')
            passowrd = data.get('password')
            email= data.get('email')
            user= User.objects.create_user(email=email,password=passowrd,username=username)
            profile=Profile.objects.create(user=user)
            user.save()
            profile.save()
            return JsonResponse({"status":"succes"})
        except:
            return JsonResponse({"status":"error"})
    else :
        return JsonResponse({"status":"unexcepected request"})
@csrf_exempt
def postplayer(request) :
    if request.method=='POST' :
        try :
            data = json.loads(request.body)
            id=data['id']
            user=data['user']
            balance=data['balance']
            sub=data['subs']
            squad=Profile.objects.get(pk=user)
            squad.current_balance=balance
            squad.substitution["subs"]=sub
            squad.squad['squad']=id
            squad.save()
            return JsonResponse({"status":"succes"})
        except :
            return JsonResponse({"status":"fail"})
    else :
        return JsonResponse({"status":"unexcepectedrequest"})
@csrf_exempt
def substitution(request):
    if request.method=='POST' :
        try :
            data = json.loads(request.body)
            sub=data['sub']
            tripple=data['tripple']
            bench=data['bench']
            captin=data['captin']
            vice=data['vice']
            user=data['user']
            subs=Profile.objects.get(pk=user)
            subs.substitution['subs']=sub
            subs.benchboast=bench
            subs.tripplecaptin=tripple
            subs.captin=captin
            subs.vice=vice
            subs.save()
            return JsonResponse({"status":"succes"})
        except :
            return JsonResponse({"status":"fail"})
    else :
        return JsonResponse({"status":"unexcepectedrequest"})
def post_players_point(request,type) :
    users=Profile.objects.all()
    round=LeagueInfo.objects.get().current_round
    for k in users :
        l=[]
        squad=k.squad['squad']
        for i in squad :
            player_team_obj=Player.objects.get(pk=i).team
            team_obj=Team.objects.get(name=player_team_obj)
            li=list(team_obj.pointsystem['pointsystem'][round-1]['events'])
            for j in li :
                if j['id']==i :
                    l.append(j)
        if type=="add" and len(k.round_stataics['statics'])<round :
            k.round_stataics['statics'].append(l)
            k.save()
            return JsonResponse({"result" : "data was added"})
        elif type=="update" :
            k.round_stataics['statics'][round]=l
            k.save()
            return JsonResponse({"result" : "data was updated"})
        else :
            return JsonResponse({"result":"undefined request"})
# Create your views here.