from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from .forms import UserForm
from .models import UserModel
from django.urls import reverse

# Create your views here.
def todo_home(request):
    return render(request, 'todo/home.html')

class SignupView(View):
    def get(self, request):
        print(request.get_full_path())
        return render(request, 'todo/signup.html', {"present": False})
    
    def post(self, request):          
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            if UserModel.objects.filter(username=username).count() != 0:
                print(UserModel.objects.all(), '-----------------')
                return render(request, 'todo/signup.html', {'present': True})
            form.save()            
            return redirect(reverse('todo:login'))    

class LoginView(View):
    def get(self, request):
        return render(request, 'todo/login.html', {'message': ''})
    
    def post(self, request):
        user = UserModel.objects.filter(username=request.POST.get('username'))
        if user.count() == 0:
            return render(request, 'todo/login.html', {'message': 'invalid user does not exist'}, status=400)
        if user[0].password != request.POST.get('password'):
            return render(request, 'todo/login.html', {'message': 'wrong password'}, status=400)  
        print('dashboardd')              
        response = redirect(reverse('todo:dashboard'))
        response.set_cookie('logged_in', True)
        return response
    
def logout(request):
    if request.COOKIES.get('logged_in'):             
        response = HttpResponseRedirect(reverse('todo:todo-home'))
        response.delete_cookie('logged_in')
        return response
    return render(request, 'todo/invalid.html')

def dashboard(request):
    return render(request, 'todo/dashboard.html')