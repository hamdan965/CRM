from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Work
from .forms import WorkForm

import openai
import os
from dotenv import load_dotenv
load_dotenv()


def loginPage(request):

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
            messa
    context = {}
    return render(request, 'base/login_page.html', context)



def home(request):
    return render(request, 'base/home.html')

def cordinator(request):
    return render(request, 'base/cordinator.html')

def manageTasks(request):
    works = Work.objects.all()
    context = {'works':works}
    return render(request, 'base/manageTasks.html', context)

def description(request, pk):
    work = Work.objects.get(id=pk)
    context = {'work': work}
    return render(request, 'base/description.html', context)

def addTask(request):
    form = WorkForm()

    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cordinator')

    context = {'form':form}
    return render(request, 'base/addtask.html', context)


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

def deleteTask(request, pk):
    work = Work.objects.get(id=pk)
    if request.method == 'POST':
        work.delete()
        return redirect('manageTasks')
    return render(request, 'base/deleteTask.html', {'obj':work})



api_key = os.getenv("OPENAI_KEY", None)

def test(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role":"user", "content":prompt}
            ],
            max_tokens = 256,
            temperature = 0.5
            )
        print(completion)
        chatbot_response = completion.choices[0].message['content']
    return render(request, 'base/test.html',{"response": chatbot_response})
        

