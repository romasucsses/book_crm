from django.shortcuts import redirect, reverse


class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.resolver_match is not None and request.resolver_match.url_name not in ['login', 'signup']:
            return redirect(reverse('login'))
        response = self.get_response(request)
        return response

