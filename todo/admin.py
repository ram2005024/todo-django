from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display=('task','is_completed')
    search_fields=('task',)