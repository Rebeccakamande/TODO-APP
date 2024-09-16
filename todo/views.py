from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from .models import Task


# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        updated_Task = request.POST['task']
        get_task.task = updated_Task
        get_task.save()
        return redirect('home')

    else:
        context = {
            'get_task': get_task
        }
        return render(request,'editTask.html', context)
    
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')