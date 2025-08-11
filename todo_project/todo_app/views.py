from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def hello(request):
    return HttpResponse("This is our basic todo app")

def index(request):
    context = {
        'name': 'Charlie',
    }
    return render(request, 'todo_app/index.html', context) 

def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 5, orphans=2, allow_empty_first_page=True)
    page = request.GET.get('page')

    try:
        paginated_tasks = paginator.page(page)
    except PageNotAnInteger:
        paginated_tasks = paginator.page(1)
    except EmptyPage:
        paginated_tasks = paginated_tasks.page(paginator.num_pages)


    return render(request, 'todo_app/list.html', {'tasks': paginated_tasks})

def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'todo_app/detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TaskCreateForm()
    return render(request, 'todo_app/create.html', {'form': form})

def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail', id=task.id)
    else:
        form = TaskCreateForm(instance=task)
    return render(request, 'todo_app/update.html', {'form': form})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    return render(request, 'todo_app/delete.html', {'task': task})