from django.shortcuts import render, redirect
from .models import Work
from .forms import WorkForm

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
        

