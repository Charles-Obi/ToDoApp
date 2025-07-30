from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("This is our basic todo app")

def index(request):
    context = {
        'name': 'Charlie',
    }
    return render(request, 'todo_app/index.html', context) 