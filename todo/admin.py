from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_complete', 'updatead_at')

# Register your models here.
admin.site.register(Task, TaskAdmin)
