from django.shortcuts import render
from .models import Info

def send_message(request):
    myinfo = Info.objects.first()
    return render(request, 'contact/contact.html', {'myinfo':myinfo})