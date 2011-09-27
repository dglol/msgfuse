from django.http import HttpResponse
from appcore.models import *
from appcore.forms import *
from django.shortcuts import render_to_response

import datetime

def homepage(request):
    now = datetime.datetime.now()
    if request.method =='POST':
        msgform = MessageForm(request.POST)
        if form.is_valid():
            content = requst.POST['msgValue']
            p = Messages(content=content, dateCreated=now)
        return render_to_response('homepage.html',{
        'msgform': msgform,
        })
    else:
        msgform = MessageForm()
        return render_to_response('homepage.html',{
        'msgform': msgform,
        })
            
#def linkpage(request, Hash_id):



