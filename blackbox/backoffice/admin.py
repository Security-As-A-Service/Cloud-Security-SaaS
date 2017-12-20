# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import AppList
from .models import ServerList
from .models import Pentest
from .models import CodeAnalyse
from .models import QualysAnalyse
from .models import Vulnerability
from .models import Comment


#admin.site.register(AppList)
#admin.site.register(ServerList)
#admin.site.register(Pentest)
#admin.site.register(CodeAnalyse)
#admin.site.register(QualysAnalyse)
#admin.site.register(Vulnerability)
#admin.site.register(Comment)

@admin.register(AppList)
class AppListAdmin(ImportExportModelAdmin):
    pass

@admin.register(Vulnerability)
class VulnerabilityAdmin(ImportExportModelAdmin):
    pass

@admin.register(ServerList)
class ServerListAdmin(ImportExportModelAdmin):
    pass

@admin.register(CodeAnalyse)
class CodeAnalyse(ImportExportModelAdmin):
    pass

@admin.register(Pentest)
class PentestAdmin(ImportExportModelAdmin):
    pass

@admin.register(QualysAnalyse)
class QualysAnalyseAdmin(ImportExportModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    pass
