from django.core.context_processors import csrf
from django.db.models import Q
from django.http import HttpResponse, Http404
from appcore.models import *
from appcore.forms import *
from scripts import rsg
from django.shortcuts import render_to_response
import datetime

def homepage(request):
    now = datetime.datetime.now()
    hashCode = ""
    hashCodeAdmin = ""
    if request.method =='POST':
        msgform = MessageForm(request.POST)
        viewform = ViewForm(request.POST)
        if msgform.is_valid() & viewform.is_valid():
            while True:
                hashCode = rsg.generate()
                hashCodeAdmin = rsg.generate()
                r = Messages.objects.filter(Q(hashCode=hashCode) 
                | Q(hashCodeAdmin = hashCode)
                | Q(hashCode = hashCodeAdmin)
                | Q(hashCodeAdmin = hashCodeAdmin))
                if r.count() == 0:
                    break;
                    
            content = request.POST['msgValue']
            requiredViews = request.POST['RequiredViews']
            closingViews = request.POST['ClosingViews']
            
            p = Messages(content=content,
            dateCreated=now,
            hashCode = hashCode,
            hashCodeAdmin = hashCodeAdmin,
            initDate=now,
            requiredClickNumber=requiredViews,
            closingClickNumber=closingViews)
            
            p.save()
            hashCode = "Your Link: msgfuse.com/%s" %hashCode
            hashCodeAdmin = "Your Admin Link: msgfuse.com/%s" %hashCodeAdmin
            
        return render_to_response('homepage.html',{
        'msgform': msgform,
        'viewform': viewform,
        'hashCode': hashCode,
        'hashCodeAdmin': hashCodeAdmin,
        })
    else:
        msgform = MessageForm()
        viewform = ViewForm()
        return render_to_response('homepage.html',{
        'msgform': msgform,
        'viewform': viewform,
        })
            
def linkpage(request, hashCode):
    try:
        r = Messages.objects.get(hashCode=hashCode)
    except:
        raise Http404

    if r.hashCode == hashCode:    
        r.messageClicks += 1
        r.save()
        if r.requiredClickNumber <= r.messageClicks <= r.closingClickNumber:
            return render_to_response('linkpage.html',{'content': '%s' %r.content})
        elif r.closingClickNumber < r.messageClicks:
            return render_to_response('linkpage.html',{'content': 'Link just expired!'})
        else:    
            return render_to_response('linkpage.html',{'content': 'Comeback Another Time!'}) 
    else:
        raise Http404

def linkadmin(request, hashCode):
    try:
        r = Messages.objects.get(hashCodeAdmin=hashCode)
    except:
        raise Http404

    if r.hashCodeAdmin == hashCode:
        views = '%s' %r.messageClicks
        if r.requiredClickNumber <= r.messageClicks <= r.closingClickNumber:
            return render_to_response('linkAdmin.html',{
            'views': views,
            'status': 'Active',
            })
        elif r.closingClickNumber < r.messageClicks:
            r.delete()
            return render_to_response('linkAdmin.html',{
            'views': views,
            'status': 'Link just expired! Both links will be deleted',
            })
        else:    
            return render_to_response('linkAdmin.html',{
            'views': views,
            'status': 'Inactive',
            })
    else:
        raise Http404


