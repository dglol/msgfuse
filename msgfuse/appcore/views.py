from django.core.context_processors import csrf
from django.http import HttpResponse
from appcore.models import *
from appcore.forms import *
from django.shortcuts import render_to_response

import datetime

def homepage(request):
    now = datetime.datetime.now()
    if request.method =='POST':
        msgform = MessageForm(request.POST)
        if msgform.is_valid():
            content = request.POST['msgValue']
            p = Messages(content=content, dateCreated=now, hashCode = "12345", initDate=now)
            p.save()
        #return HttpResponse("<p>hi</p>")
        return render_to_response('homepage.html',{
        'msgform': msgform,
        })
    else:
        msgform = MessageForm()
        return render_to_response('homepage.html',{
        'msgform': msgform,
        })
            
#def linkpage(request, Hash_id):



