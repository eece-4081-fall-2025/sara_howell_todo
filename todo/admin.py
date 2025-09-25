from django.contrib import admin
from .models import ToDo

# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['name', 'complete', 'due_date']
    list_filter = ['complete', 'due_date']
    search_fields = ['name']
    