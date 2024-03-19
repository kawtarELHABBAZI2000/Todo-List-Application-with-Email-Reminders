from django.urls import path
from .views import list_todo, todo_detail

urlpatterns = [
    path('', list_todo, name='list-todo'),
    path('<int:pk>/', todo_detail, name='todo-detail'),
]