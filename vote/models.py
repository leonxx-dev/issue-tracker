from django.db import models
from django.conf import settings
from django.utils import timezone
from tickets.models import Ticket

class Vote(models.Model):
    vote_for = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True, null=True)
    
    class Meta:
        unique_together = ('vote_for', 'voter')
    
    def __str__(self):
        return self.published_date

