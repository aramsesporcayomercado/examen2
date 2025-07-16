from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todos:list')

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todos:list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todos/confirm_delete.html'
    success_url = reverse_lazy('todos:list')

class TodosOnlyIDs(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    def get_queryset(self):
        return Todo.objects.values('id')

class TodosIDsAndTitles(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    def get_queryset(self):
        return Todo.objects.values('id', 'title')

class TodosPending(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    def get_queryset(self):
        return Todo.objects.filter(completed=False).values('id', 'title')

class TodosCompleted(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    def get_queryset(self):
        return Todo.objects.filter(completed=True).values('id', 'title')

class TodosIDsAndUserID(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    def get_queryset(self):
        return Todo.objects.values('id', 'user_id')

class TodosCompletedWithUserID(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    def get_queryset(self):
        return Todo.objects.filter(completed=True).values('id', 'user_id')

class TodosPendingWithUserID(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    def get_queryset(self):
        return Todo.objects.filter(completed=False).values('id', 'user_id')
