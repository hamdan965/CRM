from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .models import Work, Employee, Client
from .forms import WorkForm, ClientForm
from .decorators import allowed_users


# import openai
import os
from dotenv import load_dotenv
load_dotenv()


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'User does not Exist')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username Or Password Does not Exist')


    context = {}
    return render(request, 'base/login_page.html', context)

def navprofile(request):
    context = {}
    return render(request, 'base/navprofile.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# @login_required(login_url='login')
def home(request):
    return render(request, 'base/home.html')

# @login_required(login_url='login')
def manageTasks(request):
    works = Work.objects.all().order_by('dueDate')
    context = {'works':works}
    return render(request, 'base/manageTasks.html', context)

def clientinfo(request):
    clients = Client.objects.all()
    context = {'clients' : clients}
    return render(request, 'base/clientinfo.html', context)

# @login_required(login_url='login')
def employees(request):
    employeesUsers = Employee.objects.all()
    context = {'employeesUsers':employeesUsers}
    return render(request, 'base/employees.html', context)

# @login_required(login_url='login')
def description(request, pk):
    work = Work.objects.get(id=pk)
    context = {'work': work}
    return render(request, 'base/description.html', context)

# @login_required(login_url='login')
def addTask(request):
    form = WorkForm()

    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manageTasks')

    context = {'form':form}
    return render(request, 'base/addtask.html', context)

def addclient(request):
    form = ClientForm()

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addclient')
        
    context = {'form': form}
    return render(request, 'base/addclient.html')

# @login_required(login_url='login')
def updateTask(request, pk):
    work = Work.objects.get(id=pk)
    form = WorkForm(instance=work)

    if request.method == 'POST':
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('manageTasks')
        
    context = {'form': form}
    return render(request, 'base/addtask.html', context)

# @allowed_users(allowed_roles=[settings.ADMIN_GROUP])
# @login_required(login_url='login')
def deleteTask(request, pk):
    work = Work.objects.get(id=pk)
    if request.method == 'POST':
        work.delete()
        return redirect('manageTasks')
    return render(request, 'base/deleteTask.html', {'obj':work})



# api_key = os.getenv("OPENAI_KEY", None)

# def test(request):
#     chatbot_response = None
#     if api_key is not None and request.method == 'POST':
#         openai.api_key = api_key
#         user_input = request.POST.get('user_input')
#         prompt = user_input

#         completion = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages = [
#                 {"role":"user", "content":prompt}
#             ],
#             max_tokens = 256,
#             temperature = 0.5
#             )
#         print(completion)
#         chatbot_response = completion.choices[0].message['content']
#     return render(request, 'base/test.html',{"response": chatbot_response})
        

