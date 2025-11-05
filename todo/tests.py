from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import ToDo
from .forms import TodoForm, QuickAddForm


class ToDoModelTests(TestCase):
    """Test cases for the ToDo model"""
    
    def setUp(self):
        """Set up test data"""
        self.today = timezone.now().date()
        self.yesterday = self.today - timedelta(days=1)
        self.tomorrow = self.today + timedelta(days=1)
    
    def test_todo_creation(self):
        """Test creating a basic todo"""
        todo = ToDo.objects.create(
            name="Test Task",
            status="pending"
        )
        self.assertEqual(todo.name, "Test Task")
        self.assertEqual(todo.status, "pending")
        self.assertIsNone(todo.due_date)
    
    def test_todo_str_method(self):
        """Test the string representation of a todo"""
        todo = ToDo.objects.create(name="Test Task")
        self.assertEqual(str(todo), "Test Task")
    
    def test_todo_default_status(self):
        """Test that default status is 'pending'"""
        todo = ToDo.objects.create(name="Test Task")
        self.assertEqual(todo.status, "pending")
    
    def test_todo_status_choices(self):
        """Test all valid status choices"""
        statuses = ['pending', 'done', 'skipped']
        for status in statuses:
            todo = ToDo.objects.create(
                name=f"Task {status}",
                status=status
            )
            self.assertEqual(todo.status, status)
    
    def test_todo_with_due_date(self):
        """Test creating a todo with a due date"""
        todo = ToDo.objects.create(
            name="Task with date",
            due_date=self.tomorrow
        )
        self.assertEqual(todo.due_date, self.tomorrow)
    
    def test_is_overdue_property_with_past_date(self):
        """Test is_overdue returns True for overdue pending tasks"""
        todo = ToDo.objects.create(
            name="Overdue Task",
            status="pending",
            due_date=self.yesterday
        )
        self.assertTrue(todo.is_overdue)
    
    def test_is_overdue_property_with_future_date(self):
        """Test is_overdue returns False for future tasks"""
        todo = ToDo.objects.create(
            name="Future Task",
            status="pending",
            due_date=self.tomorrow
        )
        self.assertFalse(todo.is_overdue)
    
    def test_is_overdue_property_with_today_date(self):
        """Test is_overdue returns False for today's tasks"""
        todo = ToDo.objects.create(
            name="Today's Task",
            status="pending",
            due_date=self.today
        )
        self.assertFalse(todo.is_overdue)
    
    def test_is_overdue_property_for_completed_task(self):
        """Test is_overdue returns False for completed overdue tasks"""
        todo = ToDo.objects.create(
            name="Completed Overdue Task",
            status="done",
            due_date=self.yesterday
        )
        self.assertFalse(todo.is_overdue)
    
    def test_is_overdue_property_for_skipped_task(self):
        """Test is_overdue returns False for skipped overdue tasks"""
        todo = ToDo.objects.create(
            name="Skipped Overdue Task",
            status="skipped",
            due_date=self.yesterday
        )
        self.assertFalse(todo.is_overdue)
    
    def test_is_overdue_property_without_due_date(self):
        """Test is_overdue returns False when no due date"""
        todo = ToDo.objects.create(
            name="No Date Task",
            status="pending"
        )
        self.assertFalse(todo.is_overdue)
    
    def test_todo_timestamps(self):
        """Test that created_at and updated_at are set"""
        todo = ToDo.objects.create(name="Test Task")
        self.assertIsNotNone(todo.created_at)
        self.assertIsNotNone(todo.updated_at)
    
    def test_todo_ordering(self):
        """Test that todos are ordered by due_date, then created_at"""
        todo1 = ToDo.objects.create(name="Future", due_date=self.tomorrow)
        todo2 = ToDo.objects.create(name="Past", due_date=self.yesterday)
        todo3 = ToDo.objects.create(name="Today", due_date=self.today)
        
        todos = list(ToDo.objects.all())
        self.assertEqual(todos[0], todo2)  # Yesterday first
        self.assertEqual(todos[1], todo3)  # Today second
        self.assertEqual(todos[2], todo1)  # Tomorrow last


class TodoFormTests(TestCase):
    """Test cases for TodoForm"""
    
    def test_todo_form_valid_data(self):
        """Test form with valid data"""
        form = TodoForm(data={
            'name': 'Test Task',
            'due_date': timezone.now().date(),
            'status': 'pending'
        })
        self.assertTrue(form.is_valid())
    
    def test_todo_form_missing_name(self):
        """Test form fails without name"""
        form = TodoForm(data={
            'due_date': timezone.now().date(),
            'status': 'pending'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
    
    def test_todo_form_optional_due_date(self):
        """Test form is valid without due_date"""
        form = TodoForm(data={
            'name': 'Test Task',
            'status': 'pending'
        })
        self.assertTrue(form.is_valid())
    
    def test_todo_form_invalid_status(self):
        """Test form fails with invalid status"""
        form = TodoForm(data={
            'name': 'Test Task',
            'status': 'invalid_status'
        })
        self.assertFalse(form.is_valid())


class QuickAddFormTests(TestCase):
    """Test cases for QuickAddForm"""
    
    def test_quick_add_form_valid(self):
        """Test quick add form with valid data"""
        form = QuickAddForm(data={
            'name': 'Quick Task',
            'due_date': timezone.now().date()
        })
        self.assertTrue(form.is_valid())
    
    def test_quick_add_form_without_date(self):
        """Test quick add form without due date"""
        form = QuickAddForm(data={
            'name': 'Quick Task'
        })
        self.assertTrue(form.is_valid())


class TodoViewTests(TestCase):
    """Test cases for Todo views"""
    
    def setUp(self):
        """Set up test client and data"""
        self.client = Client()
        self.today = timezone.now().date()
        self.yesterday = self.today - timedelta(days=1)
        self.tomorrow = self.today + timedelta(days=1)
    
    def test_todo_list_view_get(self):
        """Test todo list view loads correctly"""
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
    
    def test_todo_list_view_with_tasks(self):
        """Test todo list displays tasks"""
        todo = ToDo.objects.create(name="Test Task")
        response = self.client.get(reverse('todo_list'))
        self.assertContains(response, "Test Task")
    
    def test_todo_list_organizes_by_date(self):
        """Test that todos are organized by date categories"""
        ToDo.objects.create(name="Overdue", due_date=self.yesterday, status='pending')
        ToDo.objects.create(name="Today", due_date=self.today)
        ToDo.objects.create(name="Future", due_date=self.tomorrow)
        
        response = self.client.get(reverse('todo_list'))
        self.assertIn('todos_overdue', response.context)
        self.assertIn('todos_today', response.context)
        self.assertIn('todos_future', response.context)
        self.assertEqual(response.context['todos_overdue'].count(), 1)
        self.assertEqual(response.context['todos_today'].count(), 1)
        self.assertEqual(response.context['todos_future'].count(), 1)
    
    def test_todo_list_quick_add_post(self):
        """Test quick add form submission"""
        response = self.client.post(reverse('todo_list'), {
            'name': 'New Quick Task',
            'due_date': self.today
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(ToDo.objects.filter(name='New Quick Task').exists())
    
    def test_todo_create_view_get(self):
        """Test create view loads"""
        response = self.client.get(reverse('todo_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_form.html')
    
    def test_todo_create_view_post(self):
        """Test creating a todo via create view"""
        response = self.client.post(reverse('todo_create'), {
            'name': 'Created Task',
            'due_date': self.today,
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ToDo.objects.filter(name='Created Task').exists())
    
    def test_todo_edit_view_get(self):
        """Test edit view loads"""
        todo = ToDo.objects.create(name="Edit Me")
        response = self.client.get(reverse('todo_edit', args=[todo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_form.html')
        self.assertContains(response, "Edit Me")
    
    def test_todo_edit_view_post(self):
        """Test editing a todo"""
        todo = ToDo.objects.create(name="Original Name")
        response = self.client.post(reverse('todo_edit', args=[todo.pk]), {
            'name': 'Updated Name',
            'status': 'done'
        })
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.name, 'Updated Name')
        self.assertEqual(todo.status, 'done')
    
    def test_todo_delete_view_get(self):
        """Test delete confirmation page"""
        todo = ToDo.objects.create(name="Delete Me")
        response = self.client.get(reverse('todo_delete', args=[todo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_confirm_delete.html')
        self.assertContains(response, "Delete Me")
    
    def test_todo_delete_view_post(self):
        """Test deleting a todo"""
        todo = ToDo.objects.create(name="Delete Me")
        response = self.client.post(reverse('todo_delete', args=[todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(ToDo.objects.filter(pk=todo.pk).exists())
    
    def test_todo_mark_done(self):
        """Test marking a todo as done"""
        todo = ToDo.objects.create(name="Do Me", status="pending")
        response = self.client.get(reverse('todo_mark_done', args=[todo.pk]))
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.status, 'done')
    
    def test_todo_mark_skipped(self):
        """Test marking a todo as skipped"""
        todo = ToDo.objects.create(name="Skip Me", status="pending")
        response = self.client.get(reverse('todo_mark_skipped', args=[todo.pk]))
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.status, 'skipped')
    
    def test_todo_mark_pending(self):
        """Test marking a todo as pending (undo)"""
        todo = ToDo.objects.create(name="Undo Me", status="done")
        response = self.client.get(reverse('todo_mark_pending', args=[todo.pk]))
        self.assertEqual(response.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.status, 'pending')
    
    def test_status_transitions(self):
        """Test all status transitions work correctly"""
        todo = ToDo.objects.create(name="Status Test", status="pending")
        
        # Pending -> Done
        self.client.get(reverse('todo_mark_done', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertEqual(todo.status, 'done')
        
        # Done -> Pending
        self.client.get(reverse('todo_mark_pending', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertEqual(todo.status, 'pending')
        
        # Pending -> Skipped
        self.client.get(reverse('todo_mark_skipped', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertEqual(todo.status, 'skipped')
        
        # Skipped -> Pending
        self.client.get(reverse('todo_mark_pending', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertEqual(todo.status, 'pending')
    
    def test_404_for_nonexistent_todo(self):
        """Test that accessing non-existent todo returns 404"""
        response = self.client.get(reverse('todo_edit', args=[9999]))
        self.assertEqual(response.status_code, 404)


class TodoIntegrationTests(TestCase):
    """Integration tests for complete workflows"""
    
    def setUp(self):
        """Set up test client"""
        self.client = Client()
        self.today = timezone.now().date()
    
    def test_complete_todo_lifecycle(self):
        """Test complete lifecycle: create -> edit -> mark done -> delete"""
        # Create
        response = self.client.post(reverse('todo_create'), {
            'name': 'Lifecycle Task',
            'due_date': self.today,
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 302)
        todo = ToDo.objects.get(name='Lifecycle Task')
        
        # Edit
        response = self.client.post(reverse('todo_edit', args=[todo.pk]), {
            'name': 'Updated Lifecycle Task',
            'due_date': self.today,
            'status': 'pending'
        })
        todo.refresh_from_db()
        self.assertEqual(todo.name, 'Updated Lifecycle Task')
        
        # Mark Done
        response = self.client.get(reverse('todo_mark_done', args=[todo.pk]))
        todo.refresh_from_db()
        self.assertEqual(todo.status, 'done')
        
        # Delete
        response = self.client.post(reverse('todo_delete', args=[todo.pk]))
        self.assertFalse(ToDo.objects.filter(pk=todo.pk).exists())
    
    def test_date_based_filtering_accuracy(self):
        """Test that date-based filtering is accurate"""
        yesterday = self.today - timedelta(days=1)
        tomorrow = self.today + timedelta(days=1)
        
        # Create tasks for different dates
        overdue = ToDo.objects.create(name="Overdue", due_date=yesterday, status='pending')
        today_task = ToDo.objects.create(name="Today", due_date=self.today)
        future = ToDo.objects.create(name="Future", due_date=tomorrow)
        no_date = ToDo.objects.create(name="No Date")
        
        response = self.client.get(reverse('todo_list'))
        
        # Verify correct categorization
        self.assertIn(overdue, response.context['todos_overdue'])
        self.assertIn(today_task, response.context['todos_today'])
        self.assertIn(future, response.context['todos_future'])
        self.assertIn(no_date, response.context['todos_no_date'])
    
    def test_multiple_tasks_same_date(self):
        """Test handling multiple tasks with same due date"""
        for i in range(5):
            ToDo.objects.create(
                name=f"Task {i}",
                due_date=self.today
            )
        
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.context['todos_today'].count(), 5)