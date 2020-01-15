from django.db import models
from django.utils import timezone

# Create your models here.
class TypeName(models.Model):
    """
    Tycket type options will be used as foreign key for ticket
    """
    TYPE_OPTIONS = (
        ('Issue', 'Issue'),
        ('Feature', 'Feature'),
    )
    name = models.CharField(max_length=20, choices=TYPE_OPTIONS)
    
    def __str__(self):
        return self.name

class Ticket(models.Model):
    """
    Single ticket
    """
    STATUS_OPTIONS = (
        ('TD', 'To Do'),
        ('IP', 'In Progress'),
        ('D', 'Done'),
    )
    title = models.CharField(max_length=250)
    content = models.TextField()
    ticket_type = models.ForeignKey(TypeName, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default="TD")

    def __str__(self):
        return self.title