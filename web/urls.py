from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse('welcome')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('todo/', include('todo.urls', namespace="todo"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
