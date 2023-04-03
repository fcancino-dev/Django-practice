from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return HttpResponse('Index page')


def hello(request):
    return HttpResponse("<h2>Hola django</h2>")

def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, title):
    task = Task.objects.get(title=title)
    # task =  get_object_or_404(Task, id=id)
    return HttpResponse('tasks: %s' %task.title)

