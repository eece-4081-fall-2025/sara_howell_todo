from django.contrib import admin
from .models import ToDo

# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'due_date', 'created_at']
    list_filter = ['status', 'due_date']
    search_fields = ['name']
    list_editable = ['status']
    date_hierarchy = 'due_date'