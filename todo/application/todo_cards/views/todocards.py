from typing import List
import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from todo_cards.models import TodoCard


@method_decorator(csrf_exempt, name='dispatch')
class TodoCards(View):
    def get(self, request) -> JsonResponse:
        todo_cards: List[TodoCard] = TodoCard.objects.all().order_by('-date_created')
        response_dict: dict = {
            'todo_cards': [todo_card.to_frontend_dict() for todo_card in todo_cards]
        }
        return JsonResponse(response_dict)

    def put(self, request) -> JsonResponse:
        body = json.loads(request.body)
        todo_card: TodoCard = TodoCard.objects.get(id=body['id'])
        todo_card.modify_from_dict(body)
        return JsonResponse(todo_card.to_frontend_dict(), status=201)

    def post(self, request) -> JsonResponse:
        body = json.loads(request.body)
        todo_card: TodoCard = TodoCard.objects.create(name=body['name'], description=body['description'],
                                                      time_left=body['time_left'])
        return JsonResponse(todo_card.to_frontend_dict(), status=201)

    def delete(self, request) -> JsonResponse:
        body = json.loads(request.body)
        todo_id: int = body['id'];
        TodoCard.objects.filter(id=todo_id).delete()
        return JsonResponse({}, status=201)
