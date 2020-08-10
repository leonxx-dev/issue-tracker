from django.db import models
from tickets.models import Ticket
from django.conf import settings

# Create your models here.
class Order(models.Model):
    username = models.ForeignKey(   settings.AUTH_USER_MODEL, 
                                    on_delete=models.CASCADE, 
                                    related_name='order')
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=False)
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1}".format(
            self.ticket.id, self.amount)