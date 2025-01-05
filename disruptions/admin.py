from django.contrib import admin 
from .models import Disruption

class DisruptionAdmin(admin.ModelAdmin): 
    list_display = [ 
    "description", 
    "category",
    "section",
    "lotnum",
    "time", 
    "author", 
    ]

admin.site.register(Disruption,DisruptionAdmin) 