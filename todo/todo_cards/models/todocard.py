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

    def modify_from_dict(self, data: dict):
        self.name = data.get('name', self.name)
        self.description = data.get('description', self.description)
        self.completed = data.get('completed', self.completed)
        self.save()

    def to_frontend_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date_created': self.date_created.strftime('%Y-%m-%d %HH:%MM:%SS'),
            'time_left': self.time_left,
            'completed': self.completed
        }
