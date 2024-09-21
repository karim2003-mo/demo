import json
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
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
            "subs" : profile.substitution,
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
            for i in id :
                squad.squad['squad'].append(i)
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
            user=data['user']
            subs=Profile.objects.get(pk=user)
            subs.substitution['subs']=sub
            subs.save()
            return JsonResponse({"status":"succes"})
        except :
            return JsonResponse({"status":"fail"})
    else :
        return JsonResponse({"status":"unexcepectedrequest"})
# Create your views here.