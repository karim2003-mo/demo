import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
@csrf_exempt
def verify_account(request,email_address):
        k=0
        sender_email="kickpoint793@gmail.com"
        sender_pass="fnbv gddn segw qutx"
        receiver_email = email_address
        subject="workshop for the third day"
        body=f"https://hammer-e3g9bhd2g8dfe6b2.spaincentral-01.azurewebsites.net/accounts/done/{receiver_email}"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        data = json.loads(request.body)
        try :
            server = smtplib.SMTP('smtp.gmail.com', 587)
            print(k)
            server.starttls()  # Secure the connection
            print(k)
            server.login(sender_email, sender_pass)
            print(k)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            return JsonResponse({"result" : "the email has been sent"})
        except Exception as e :
            print(e)
            return JsonResponse({"result" : "the email has not been sent"})
def verification_done(request,receiver_email) :
    user=User.objects.get(email=receiver_email)
    profile=Profile.objects.get(user=user)
    profile.is_email_verified=True
    profile.save()
    return HttpResponse("your kick point acount has been verified successfully")