from django.shortcuts import render,redirect
from .models import Tasks
# Create your views here.
def add_task(request):
    task=request.POST['task']
    Tasks.objects.create(task=task)
    return redirect('home')