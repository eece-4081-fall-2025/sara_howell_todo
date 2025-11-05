from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('skipped', 'Skipped'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['due_date', '-created_at']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
    
    def __str__(self):
        return self.name
    
    @property
    def is_overdue(self):
        if self.due_date and self.status == 'pending':
            return self.due_date < timezone.now().date()
        return False