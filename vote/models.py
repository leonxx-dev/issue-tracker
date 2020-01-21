from django.db import models
from django.conf import settings
from tickets.models import Ticket

class Vote(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    vote = models.BooleanField(default=False)
    
    def __str__(self):
        return "{0}-{1}".format(self.id, self.ticket_id)

