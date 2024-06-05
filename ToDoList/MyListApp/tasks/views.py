from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Task
from django.contrib import messages
from .forms import TaskForm


def index(request):
    # tasks = Task.objects.order_by('priority', 'due_date')
    tasks = Task.objects.filter(completed=False)

    task_count = tasks.count()
    form = TaskForm()
    return render(request, 'tasks/index.html', {
        'tasks': tasks, 
        'form': form,
        'task_count': task_count,
    })


# @require_POST
def add_task(request):
    form = TaskForm

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task has been added successfully")
            return redirect('tasks:index')
        
    return render(request, "tasks/add_task.html", {
            "form": form,
    })

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    messages.success(request, "Task completed, weldone fam !")
    return redirect('tasks:index')


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('tasks:index')


def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/all_tasks.html", {
        'tasks': tasks,
    })