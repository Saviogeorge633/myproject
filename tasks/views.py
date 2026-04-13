from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(
                title=title,
                user=request.user   
            )
        return redirect('/')  
    
    tasks = Task.objects.filter(user=request.user)

    
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)


    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    pending = tasks.filter(completed=False).count()

    return render(request, 'tasks/home.html', {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending
    })

def complete(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = not task.completed   
    task.save()
    return redirect('/')

def delete(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('/')

def edit(request, id):
    task = Task.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task.title = title
            task.save()
            return redirect('/')

    return render(request, 'tasks/edit.html', {'task': task})