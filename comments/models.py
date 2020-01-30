from django.db import models
from django.conf import settings
from django.utils import timezone
from tickets.models import Ticket

class Comment(models.Model):
    
    comment_on = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.comment_author)
