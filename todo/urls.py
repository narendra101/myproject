from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_home, name="todo-home"),
    path('signup/', views.SignupView.as_view(), name="sign-up"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
]