from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Tasks
# Home
def home(request):
   completed_tasks=Tasks.objects.filter(is_completed=True)
   incomplete_tasks=Tasks.objects.filter(is_completed=False).order_by('-created_at')
   context={
      'comp_task':completed_tasks,
      'incomp_task':incomplete_tasks
   }
   return render(request,'home.html',context)