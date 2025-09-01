from django.shortcuts import render,HttpResponse,redirect
from .models import Task
# Create your views here.

def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    
    return render (request,'home.html',{"tasks":tasks})

def addtask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
