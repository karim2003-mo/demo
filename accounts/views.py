from django.shortcuts import render
import json
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
@csrf_exempt
def login(request) :
    if request.method=='POST' :
        try :
            data = json.loads(request.body)
            username = data.get('username')
            passowrd = data.get('password')
            user= authenticate(username,passowrd)
            if user is not None :
                x_user=User.objects.get(username=username)
                profile_data=Profile.objects.get(user=x_user)
                return JsonResponse({"status":"succes",
                                    "account":{
                                        "score":profile_data.score,
                                        "favourite club":profile_data.favourite_club,
                                    }})
            else :
                return JsonResponse({"status":"fail",})
        except:
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
