from datetime import datetime
from typing import List

from django.http import JsonResponse
from django.views.generic import View

from todo_cards.models import TodoCard


class TodoCards(View):
    def get(self, request) -> JsonResponse:
        todo_cards: List[TodoCard] = TodoCard.objects.all()
        response_dict: dict = {
            'todo_cards':
            [{
                    'id': todo_card.pk,
                    'name': todo_card.name,
                    'description': todo_card.description,
                    'date_created': todo_card.date_created.strftime('%Y-%m-%d %HH:%MM:%SS'),
                    'time_left': todo_card.time_left.strftime('%HH:%MM'),
                    'completed': todo_card.completed
                 } for todo_card in todo_cards]
        }
        return JsonResponse(response_dict)