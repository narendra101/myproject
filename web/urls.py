from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse('welcome')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('todo/', include('todo.urls', namespace="todo"))
]
