from django.urls import path
from . import views
urlpatterns = [
    path('add-task',views.add_task,name="add_task"),
    path('mark_as_done/<int:id>',views.mark_as_done,name="mark_task_done"),
    path('mark_as_undone/<int:id>',views.mark_task_undo,name="mark_task_undone"),
    path('delete_task/<int:id>',views.delete_task,name="delete_task"),
    path('edit_task/<int:id>',views.edit_task,name="edit_task")
]
