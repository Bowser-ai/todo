from datetime import datetime, time

from django.db import models


class TodoCard(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=datetime.now)
    time_left = models.TimeField(default=time.fromisoformat('08:00:00'))
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
