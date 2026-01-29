from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks
# Create your views here.
def add_task(request):
    task=request.POST['task']
    Tasks.objects.create(task=task)
    return redirect('home')

# view for marking the task as done
def mark_as_done(request,id):
    task=get_object_or_404(Tasks,id=id)
    task.is_completed=True
    task.save()
    return redirect('home')

# view for marking the task as undo  
def mark_task_undo(request,id):
    task=get_object_or_404(Tasks,id=id)
    task.is_completed=False
    task.save()
    return redirect('home')

# View for deleting the task
def delete_task(request,id):
    task=get_object_or_404(Tasks,id=id)
    task.delete()
    return redirect('home')

#View for editing the task
def edit_task(request,id):
    task=get_object_or_404(Tasks,id=id)
    if request.method=='GET':
        context={
            'task':task
        }
        return render(request,'edit_task_html.html',context)
    else:
        request.method=='POST'
        new_task=request.POST['new_text']
        task.task=new_task
        task.save()
        return redirect('home')

