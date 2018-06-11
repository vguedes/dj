from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete="CASCADE")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Ticker {}".format(self.id)
