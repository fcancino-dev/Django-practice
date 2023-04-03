from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('hello/', views.hello),
    path('projects/', views.projects),
    path('tasks/<str:title>', views.tasks),
]
