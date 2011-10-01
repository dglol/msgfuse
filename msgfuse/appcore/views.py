from django.core.context_processors import csrf
from django.http import HttpResponse
from appcore.models import *
from appcore.forms import *
from scripts import rsg
from django.shortcuts import render_to_response
import datetime

def homepage(request):
    now = datetime.datetime.now()
    if request.method =='POST':
        msgform = MessageForm(request.POST)
        viewform = ViewForm(request.POST)
        if msgform.is_valid() & viewform.is_valid():
            while True:
                hashCode = rsg.generate()
                r = Messages.objects.filter(hashCode=hashCode)
                if r.count() == 0:
                    break;
            content = request.POST['msgValue']
            requiredViews = request.POST['RequiredViews']
            closingViews = request.POST['ClosingViews']
            p = Messages(content=content, dateCreated=now, hashCode = hashCode, initDate=now, requiredClickNumber=requiredViews, closingClickNumber=closingViews)
            p.save()
            hashCode = "Your Link: msgfuse.com/%s" %hashCode
        return render_to_response('homepage.html',{
        'msgform': msgform,
        'viewform': viewform,
        'hashCode': hashCode,
        })
    else:
        msgform = MessageForm()
        viewform = ViewForm()
        return render_to_response('homepage.html',{
        'msgform': msgform,
        'viewform': viewform,
        })
            
# def linkpage(request, Hash_id):



