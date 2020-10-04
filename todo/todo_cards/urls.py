from django.urls import path

from todo_cards.views import TodoCards

urlpatterns = [
    path('', TodoCards.as_view(), name='todo-cards'),
]