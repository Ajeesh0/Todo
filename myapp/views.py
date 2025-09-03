from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Task
# Create your views here.

def home(request):

    # for incomplete tasks
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')

    # for completed tasts

    completed_task=Task.objects.filter(is_completed=True)
    
    context={

         "tasks":tasks,

          "completed_task":completed_task
    }
    
    return render (request,'home.html',context)

def addtask(request):
    task=request.POST['task']

    Task.objects.create(task=task)
    return redirect('home')

def Mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def Mark_as_Undo(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')


def Edit_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
    
        new_task=request.POST['task'] 
        get_task.task=new_task
        get_task.save()
        return redirect('home') 
    else:
        context={
            'get_task':get_task
        }

        
    
    return render(request,'edit_task.html',context)


def Delete_task(request,pk):

    delete_task=get_object_or_404(Task,pk=pk)

    delete_task.delete()

    return redirect('home')
