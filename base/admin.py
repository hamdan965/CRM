from django.contrib import admin

# Register your models here.

from .models import Client, Employee, Work 

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Work)