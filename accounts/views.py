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
            User= authenticate(username,passowrd)
            if User is not None :
                return JsonResponse({"status":"succes"})
            else :
                return JsonResponse({"status":"fail"})
        except:
            return JsonResponse({"status":"error"})
@csrf_exempt
def signup(request) :
    if request.method=='POST' :
        try :
            data = json.loads(request.body)
            username = data.get('username')
            passowrd = data.get('passwrd')
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
