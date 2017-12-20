from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [

    #url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.urls)),
      
    url(r'^$', views.index, name='index'),
    
    #url(r'dashboard/$', views.search, name='search'),
    url(r'dashboard/$', views.dashboard, name='dashboard'),

    url(r'server/$', views.server, name='server'),
    url(r'pentest/$', views.pentest, name='pentest'),
    url(r'vulnerability/$', views.vulnerability, name='vulnerability'),
    url(r'^(?P<applist_id>[0-9]+)/server/refcard/$', views.srefcard, name='srefcard'),
    
    url(r'application/$', views.application, name='application'),
    
    url(r'^(?P<applist_id>[0-9]+)/refcard/$', views.refcard, name='refcard'),
    #ex: /dashboard/5/
  
    
    url(r'^(?P<applist_id>[0-9]+)/search/$', views.search, name='search'),
    #ex: /polls/5/vote/
    url(r'^(?P<applist_id>[0-9]+)/home/$', views.home, name='home'),
]
