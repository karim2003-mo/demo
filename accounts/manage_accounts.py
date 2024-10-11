import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
def verification_done(request,receiver_email) :
    user=User.objects.get(email=receiver_email)
    profile=Profile.objects.get(user=user)
    profile.is_email_verified=True
    profile.save()
    return HttpResponse("your kick point acount has been verified successfully")