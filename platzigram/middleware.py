from django.shortcuts import redirect
from django.urls import reverse
from django.urls import re_path

class ProfileCompletionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_staff:
            if not request.user.is_anonymous:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')
        
        response = self.get_response(request)
        return response

class LoggedInMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            if request.path == reverse('users:login'):
                return redirect('posts/feed')
        
        response = self.get_response(request)
        return response