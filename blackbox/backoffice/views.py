# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import AppList, Pentest, ServerList, CodeAnalyse, QualysAnalyse, Vulnerability, Comment
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    ApplicationList = AppList.objects.order_by('Appname')[:100]
    serverlist = ServerList.objects.order_by('servername')[:100]
    context = {'ApplicationList': ApplicationList, 'ServerList': serverlist}
    return render(request, 'backoffice/index.html', context)
    #return render(request, 'registration/login.html')

@login_required
def application(request):
    ApplicationList = AppList.objects.order_by('Appname')[:100]
    context = {'ApplicationList': ApplicationList}
    return render(request, 'backoffice/application.html', context)
    #return render(request, 'registration/login.html')

@login_required
def server(request):
    serverlist = ServerList.objects.order_by('servername')[:100]
    context = {'ServerList': serverlist}
    return render(request, 'backoffice/server.html', context)
    #return render(request, 'registration/login.html')

@login_required
def pentest(request):
    PentestList = Pentest.objects.order_by('name')[:100]
    context = {'PentestList': PentestList}
    return render(request, 'backoffice/pentest.html', context)
    #return render(request, 'registration/login.html')
    
@login_required
def vulnerability(request):
    VulnList = Vulnerability.objects.order_by('id')[:100]
    context = {'VulnList': VulnList}
    return render(request, 'backoffice/vulnerability.html', context)
    #return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    ApplicationList = AppList.objects.order_by('Appname')[:10000000]
    AppListSize = AppList.objects.count()
    serverlist = ServerList.objects.order_by('servername')[:100000000]
    pentestlist = Pentest.objects.order_by('name')[:100000000]
    codeanalyse = CodeAnalyse.objects.order_by('name')[:100000000]
    qualysanalyse = QualysAnalyse.objects.order_by('name')[:100000000]
    vulnerabilitylist = Vulnerability.objects.order_by('name')[:100000000]
    comments = Comment.objects.order_by('name')[:100000000]
    NbrApp = ApplicationList.count()
    NbrServ = serverlist.count()
    NbrVuln = vulnerabilitylist.count()
    NbrPentest = pentestlist.count()
    context = {
        'ApplicationList': ApplicationList,
        'ServerList': serverlist,
        'PentestList': pentestlist,
        'CodeList' : codeanalyse,
        'QualysListe' : qualysanalyse,
        'VulnList' : vulnerabilitylist,
        'NbrApp' : NbrApp,
        'NbrServ' : NbrServ,
        'NbrVuln' : NbrVuln,
        'NbrPentest' : NbrPentest,        
        }
    return render(request, 'backoffice/dashboard.html', context)

@login_required     
def srefcard(request, applist_id):
    ServCard = ServerList.objects.get(id__exact=applist_id)
    context = {'ServCard': ServCard}
    #return HttpResponse("Test : %s " % applist_id)
    return render(request, 'backoffice/refcard.html', context)

@login_required     
def refcard(request, applist_id):
    AppCard = AppList.objects.get(id__exact=applist_id)
    context = {'AppCard': AppCard}
    #return HttpResponse("Test : %s " % applist_id)
    return render(request, 'backoffice/refcard.html', context)
    
def home(request, applist_id):
    return HttpResponse("home pour %s " % applist_id)
    
@login_required   
def search(request, applist_id):
    return HttpResponse("home pour %s " % applist_id)
    
def login(request):
    return render(request, 'registration/login.html')
    


