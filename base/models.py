from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class employee(models.Model):
    name = models.CharField(max_length=200)

class Work(models.Model):
    client = models.ForeignKey(Client,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=200)
    asignee = models.CharField(max_length=200)
    progress = models.CharField(max_length=200)
    post = models.DateField()
    content = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.task



