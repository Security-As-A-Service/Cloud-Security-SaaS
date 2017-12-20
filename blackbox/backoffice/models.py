# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

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
    
    Appname = models.CharField(max_length=100, unique=True, blank=False)
    Instance = models.CharField(max_length=100, unique=True)
    server = models.ForeignKey('ServerList', null=True)
    Bamplus = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    Bamplusid = models.IntegerField(default=0, blank=True)
    url =  models.CharField(max_length=100, null=True, blank=True)
    Confidentiality = models.CharField(max_length=15, choices=LevelChoice, blank=False)
    Integrity = models.CharField(max_length=15, choices=LevelChoice, blank=False)
    Availibity = models.CharField(max_length=15, choices=LevelChoice, blank=False)
    Tracability = models.CharField(max_length=15, choices=LevelChoice, blank=False)
    ciso_perim = models.CharField(max_length=25, blank=True)
    compliant_based_ident = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    criticity_level = models.CharField(max_length=15, choices=LevelChoice, blank=False)
    Developpment = models.CharField(max_length=10, choices=IntExtChoice, blank=True)
    fsa = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    fsa_level = models.CharField(max_length=5, choices=LevelNum, blank=True)
    lpm = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    lpm_level = models.CharField(max_length=5, choices=LevelNum, blank=True)
    gsf_uptodate = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    gsf_lastdate = models.DateTimeField()
    hosting = models.CharField(max_length=15, choices=IntExtChoice)
    internet_facing = models.CharField(max_length=5, choices=YesNoChoice)
    n_tier = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    last_production_review = models.DateTimeField('production review', blank=True, null=True)
    role_base_access_control = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    sensitivity_level = models.CharField(max_length=10, choices=LevelChoice)
    siem = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    https = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    ssl = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    tls = models.CharField(max_length=5, choices=YesNoChoice, blank=True)
    #sub-perim = ...
    
    def __unicode__(self):
        return "[{1}] {0} ".format(self.Appname, self.id)
        
class ServerList(models.Model):
    IntExtChoice = (
        ('INTERNAL', 'INTERNAL'),
        ('EXTERNAL', 'EXTERNAL'),
        ('SHARE', 'SHARE'),
        )
    OsChoice = (
        ('Windows', 'Windows'),
        ('Unix', 'Unix'),
        ('Linux', 'Linux'),
        ('Macintosh', 'Macintosh'),
        )
    
    servername = models.CharField(max_length=100, unique=True, blank=False)
    ip = models.CharField(max_length=100, unique=True)
    hosting = models.CharField(max_length=10, choices=IntExtChoice)
    os =  models.CharField(max_length=100, choices=OsChoice)
    
    #sub-perim = ...
    
    def __unicode__(self):
        return "[{1}] {0} ".format(self.servername, self.id)

class Pentest(models.Model):
    AuditorChoice = (
        ('Beijaflore', 'Beijaflore'),
        ('Nes', 'Nes'),
        ('Gfi', 'Gfi'),
        ('ISPL', 'ISPL'),
        ('AST', 'AppSecTeam'),
        )
    PiloteChoice = (
        ('dla', 'Damien Lallement'),
        ('ala', 'Alexandre Lasnier'),
        ('...', '...'),
        )
    YesNoChoice = (
        ('YES', 'YES'),
        ('NO', 'NO'),
        )
        
    name   = models.CharField(max_length=100)
    target = models.ForeignKey('AppList')
    nbr_Day    = models.IntegerField(default=0)
    start_date    = models.DateTimeField()
    auditor = models.CharField(max_length=15, choices=AuditorChoice, default='null')
    pilote = models.CharField(max_length=15, choices=PiloteChoice, default='null')
    total_vulnerability = models.IntegerField(default=0)
    critical_vulnerability = models.IntegerField(default=0)
    high_vulnerability = models.IntegerField(default=0)
    medium_vulnerability = models.IntegerField(default=0)
    low_vulnerability = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "[{0}] {1} (Target :{2})".format(self.id, self.name, self.target.Appname)
        
class CodeAnalyse(models.Model):
    AuditorChoice = (
        ('BF', 'Beijaflore'),
        ('Nes', 'Nes'),
        ('Gfi', 'Gfi'),
        ('ISPL', 'ISPL'),
        ('AST', 'AppSecTeam'),
        )
    PiloteChoice = (
        ('dla', 'Damien Lallement'),
        ('ala', 'Alexandre Lasnier'),
        ('...', '...'),
        )
    YesNoChoice = (
        ('YES', 'YES'),
        ('NO', 'NO'),
        )
        
    name   = models.CharField(max_length=100)
    target = models.ForeignKey('AppList')
    nbr_Day    = models.IntegerField(default=0)
    start_date    = models.DateTimeField()
    auditor = models.CharField(max_length=15, choices=AuditorChoice, default='null')
    pilote = models.CharField(max_length=15, choices=PiloteChoice, default='null')
    total_vulnerability = models.IntegerField(default=0)
    critical_vulnerability = models.IntegerField(default=0)
    high_vulnerability = models.IntegerField(default=0)
    medium_vulnerability = models.IntegerField(default=0)
    low_vulnerability = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "[{0}] {1} (Target :{2})".format(self.id, self.name, self.target.Appname)
        
class QualysAnalyse(models.Model):
    AuditorChoice = (
        ('BF', 'Beijaflore'),
        ('Nes', 'Nes'),
        ('Gfi', 'Gfi'),
        ('ISPL', 'ISPL'),
        ('AST', 'AppSecTeam'),
        )
    PiloteChoice = (
        ('dla', 'Damien Lallement'),
        ('ala', 'Alexandre Lasnier'),
        ('...', '...'),
        )
    YesNoChoice = (
        ('YES', 'YES'),
        ('NO', 'NO'),
        )
        
    name   = models.CharField(max_length=100)
    target = models.ForeignKey('AppList')
    nbr_Day    = models.IntegerField(default=0)
    start_date    = models.DateTimeField()
    auditor = models.CharField(max_length=15, choices=AuditorChoice, default='null')
    pilote = models.CharField(max_length=15, choices=PiloteChoice, default='null')
    total_vulnerability = models.IntegerField(default=0)
    critical_vulnerability = models.IntegerField(default=0)
    high_vulnerability = models.IntegerField(default=0)
    medium_vulnerability = models.IntegerField(default=0)
    low_vulnerability = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "[{0}] {1} (Target :{2})".format(self.id, self.name, self.target.Appname)
        
class Vulnerability(models.Model):
    LevelVuln = (
        ('Critical', 'CRITICAL'),
        ('High', 'HIGH'),
        ('Medium', 'MEDIUM'),
        ('Low', 'LOW'),
        )
    StatusRemediation = (
        ('NA', 'No Assignee'),
        ('OP', 'Open'),
        ('IP', 'In-Progress'),
        ('SB', 'Submit-for-closure'),
        ('CL', 'Clos'),
        )
        
    name = models.CharField(max_length=100)
    target = models.ForeignKey('AppList')
    scope = models.ForeignKey('Pentest')
    ref_owasp = models.IntegerField(default=0)
    vuln_id = models.IntegerField(default=0)
    description = models.CharField(max_length=400)
    scenario = models.CharField(max_length=400)
    evidence = models.CharField(max_length=400)
    action = models.CharField(max_length=400)
    
    finder = models.CharField(max_length=100)
    fixer = models.CharField(max_length=100)
    
    cve = models.IntegerField(default=0) 
    impact = models.CharField(max_length=15, choices=LevelVuln)
    risk = models.CharField(max_length=15, choices=LevelVuln)
    complexity_exploitation = models.CharField(max_length=15, choices=LevelVuln)
    complexity_remediation = models.CharField(max_length=15, choices=LevelVuln)
    priority_remediation = models.CharField(max_length=15, choices=LevelVuln)
    status_remediation = models.CharField(max_length=15, choices=StatusRemediation)
    deadline_remediation = models.DateTimeField()
    
    def __unicode__(self):
        return "[{0}] {1} (Target :{2})".format(self.id, self.name, self.target.Appname)
        
class Comment(models.Model):
    ChoiceAsset = (
        ('Infra', 'Infra'),
        ('AppList', 'AppList'),
        )
    ChoiceModule = (
        ('Pentest', 'Pentest'),
        ('CodeAnalyse', 'CodeAnalyse'),
        ('QualysAnalyse', 'QualysAnalyse'),
        ('ProductionSecurityReview', 'PSR'),
        ('UAT', 'UAT'),
        )
        
    name = models.CharField(max_length=100)
    target_link = models.ForeignKey('AppList')
    scope_link = models.ForeignKey('Pentest')
    vulnerability_link = models.ForeignKey('Vulnerability')
    text_message = models.CharField(max_length=400)
    deadline_remediation = models.DateTimeField(auto_now_add=True)
        
    def __unicode__(self):
        return "[{0}] {1} (Target :{2})".format(self.id, self.name, self.target_link.Appname)