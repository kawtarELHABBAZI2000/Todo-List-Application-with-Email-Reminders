from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    PENDING = 'Pending'
    DONE = 'Done'
    IN_PROGRESS = 'In Progress'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (DONE, 'Done'),
        (IN_PROGRESS, 'In Progress'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=PENDING)
