from django.urls import path
from .views import hello, index

#Our URL patterns for the todo_app
urlpatterns = [
    path('',hello),
    path('index/', index, name='index')
]