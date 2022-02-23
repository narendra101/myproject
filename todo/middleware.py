from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'dashboard' in request.get_full_path():
            if not request.COOKIES.get('logged_in'):
                return redirect(reverse('todo:todo-home'))
            return None

        
