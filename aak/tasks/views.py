from django.shortcuts import render, redirect

from django.http import HttpResponse

from . models import Task
from . models import Label
from . forms import TaskForm

def index(request):
    #return HttpResponse('Hello AAK Tele-Science!')
    
    form = TaskForm()
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    labels = Label.objects.all()
    context = {'tasks': tasks, "labels": labels, 'TaskForm': form}
    return render(request, 'tasks.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance = task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'TaskForm': form}
    return render(request, 'update-task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'task': task}
    return render(request, 'delete-task.html', context)