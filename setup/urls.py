from django.urls import path
from todos.views import TodoListView, TodoCreateView


urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('create/', TodoCreateView.as_view(), name='todo_create')
    ]