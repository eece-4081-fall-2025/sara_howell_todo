from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import ToDo
from .forms import TodoForm, QuickAddForm

def todo_list(request):
    """Display all todos with quick add form"""
    if request.method == 'POST':
        form = QuickAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('todo_list')
    else:
        form = QuickAddForm()
    
    # Get todos organized by date
    today = timezone.now().date()
    todos_today = ToDo.objects.filter(due_date=today)
    todos_overdue = ToDo.objects.filter(due_date__lt=today, status='pending')
    todos_future = ToDo.objects.filter(due_date__gt=today)
    todos_no_date = ToDo.objects.filter(due_date__isnull=True)
    
    context = {
        'form': form,
        'todos_today': todos_today,
        'todos_overdue': todos_overdue,
        'todos_future': todos_future,
        'todos_no_date': todos_no_date,
        'today': today,
    }
    return render(request, 'todo/todo_list.html', context)

def todo_create(request):
    """Create a new todo"""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm()
    
    context = {'form': form, 'action': 'Create'}
    return render(request, 'todo/todo_form.html', context)

def todo_edit(request, pk):
    """Edit an existing todo"""
    todo = get_object_or_404(ToDo, pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    
    context = {'form': form, 'action': 'Edit', 'todo': todo}
    return render(request, 'todo/todo_form.html', context)

def todo_delete(request, pk):
    """Delete a todo"""
    todo = get_object_or_404(ToDo, pk=pk)
    
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('todo_list')
    
    context = {'todo': todo}
    return render(request, 'todo/todo_confirm_delete.html', context)

def todo_mark_done(request, pk):
    """Mark a todo as done"""
    todo = get_object_or_404(ToDo, pk=pk)
    todo.status = 'done'
    todo.save()
    messages.success(request, f'Task "{todo.name}" marked as done!')
    return redirect('todo_list')

def todo_mark_skipped(request, pk):
    """Mark a todo as skipped"""
    todo = get_object_or_404(ToDo, pk=pk)
    todo.status = 'skipped'
    todo.save()
    messages.info(request, f'Task "{todo.name}" marked as skipped.')
    return redirect('todo_list')

def todo_mark_pending(request, pk):
    """Mark a todo as pending (undo done/skipped)"""
    todo = get_object_or_404(ToDo, pk=pk)
    todo.status = 'pending'
    todo.save()
    messages.info(request, f'Task "{todo.name}" marked as pending.')
    return redirect('todo_list')

# Search Feature

def todo_search(request):
    """Search for todos by name"""
    query = request.GET.get('q', '')
    
    if query:
        # Case-insensitive search
        results = ToDo.objects.filter(name__icontains=query)
    else:
        # Empty query returns all tasks
        results = ToDo.objects.all()
    
    context = {
        'results': results,
        'query': query,
        'count': results.count()
    }
    return render(request, 'todo/todo_search.html', context)