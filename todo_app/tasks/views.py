from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Task
from .forms import TaskForm


# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    context = {
        'tasks':tasks,
        'form':form
    }

    return render(request, 'home.html', context)
