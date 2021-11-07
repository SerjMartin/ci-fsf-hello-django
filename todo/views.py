from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.
# def say_hello(request):
#    return HttpResponse("Hello!")


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
