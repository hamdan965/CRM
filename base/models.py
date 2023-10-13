from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    profile_pic = models.ImageField(default="companylogo.png",null=True, blank=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    onBoardDate = models.DateField()
    client_pic = models.ImageField(default="companylogo.png",null=True, blank=True)

    def __str__(self):
        return self.name

class Work(models.Model):
    client = models.ForeignKey(Client,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=200)
    dueDate = models.DateField(null=True)
    asignee = models.ForeignKey(Employee,on_delete=models.SET_NULL, null=True)
    progress = models.CharField(max_length=200)
    post = models.DateField()
    content = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.task



