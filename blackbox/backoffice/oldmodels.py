# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime 

class AppList(models.Model):
    YesNoChoice = (
        ('YES', 'YES'),
        ('NO', 'NO'),
        )
    IntExtChoice = (
        ('INTERNAL', 'INTERNAL'),
        ('EXTERNAL', 'EXTERNAL'),
        ('SHARE', 'SHARE'),
        )
    LevelChoice = (
        ('4', 'EXTREME'),
        ('3', 'SERIOUS'),
        ('2', 'MODERATE'),
        ('1', 'LOW'),
        )
    LevelNum = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
        )
        
    Appname = models.CharField(max_length=100, default='null')
    Instance = models.CharField(max_length=100, default='null', unique=True)
    Bamplus = models.CharField(max_length=5, choices=YesNoChoice, default='NO')
    Bamplusid = models.IntegerField(default=0, unique=True)
    Confidentiality = models.CharField(max_length=15, choices=LevelChoice, default=0)
    Integrity = models.CharField(max_length=15, choices=LevelChoice, default=0)
    Availibity = models.CharField(max_length=15, choices=LevelChoice, default=0)
    Tracability = models.CharField(max_length=15, choices=LevelChoice, default=0)
    ciso_perim = models.CharField(max_length=25, default='null')
    compliant_based_ident = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    criticity_level = models.CharField(max_length=15, choices=LevelChoice, default=0)
    Developpment = models.CharField(max_length=10, choices=IntExtChoice, default='null')
    fsa = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    fsa_level = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    gsf_uptodate = models.CharField(max_length=5, choices=YesNoChoice, default='null')
#    gsf_lastdate = DateTimeField(auto_now_add=False, blank=True)
    hosting = models.CharField(max_length=15, choices=IntExtChoice, default='null')
    https = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    internet_facing = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    n_tier = models.CharField(max_length=5, choices=YesNoChoice, default='null')
 #   production_review = DateTimeField(auto_now_add=False, blank=True)
    role_base_access_control = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    sensitivity_level = models.CharField(max_length=10, choices=LevelChoice, default='null')
    siem = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    ssl = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    tls = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    waf = models.CharField(max_length=5, choices=YesNoChoice, default='null')
    #sub-perim = ...
    
    def __unicode__(self):
        return "{0} [{1}]".format(self.Appname, self.id)

class Pentest(models.Model):
    name = models.CharField(max_length=100, default='null')
    product = models.ForeignKey('AppList')
    nbr_jour = models.IntegerField()
    #start_date = models.DateTimeField(default=False, blank=True)
    #start_date = models.DateTimeField(auto_now_add=False, blank=True)
    
    def __unicode__(self):
        return "{0} {{1}}".format(self.product.Appname, self.name)