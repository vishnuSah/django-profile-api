from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        
        return redirect('/')
    
    tasks = Task.objects.all().order_by('completed')
    form = TaskForm()
    context = {
        'tasks':tasks,
        'form':form
    }

    return render(request, 'home.html', context)

def update(request, pk):
    #print(pk)
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    form = TaskForm(instance=task)
    context = {
        'form': form
    }
    return render(request, 'update_task.html', context)

def delete(request, pk):
    #print(pk)
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()

        return redirect('/')
  
    context = {
        'task':task
    } 

    return render(request, 'delete_task.html', context)

    
