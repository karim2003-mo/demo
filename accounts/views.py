import json
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
def profile_data(request,id) :
    profile=Profile.objects.get(pk=id)
    data={"status" : "succes",
          "userdata" :{
              "username" :profile.user.username,
              "squad name" : profile.squad_name,
              "squad":profile.squad["squad"],
              "score" :profile.score["score"],
              "favourite club" :profile.favourite_club,
              "leagues":profile.leagues['leagues'],
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
# Create your views here.