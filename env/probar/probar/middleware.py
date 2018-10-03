from django.shortcuts import redirect
from django.urls import reverse


class ProfileAdminMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            profile = request.user.profile
            if profile.is_admin == False:
                if request.path == reverse('administracion'):
                    return redirect('inicio')

        response = self.get_response(request)
        return response
