from django.contrib import admin

# Register your models here.

from .models import Work, Client

admin.site.register(Work)
admin.site.register(Client)