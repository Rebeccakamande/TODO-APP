from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_complete=False).order_by("-updatead_at")
    completedTasks = Task.objects.filter(is_complete=True)
    context = {
        'tasks': tasks,
        'completedTasks':completedTasks
    }
    return render(request, 'home.html', context)