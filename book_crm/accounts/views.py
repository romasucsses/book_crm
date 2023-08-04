from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('all_books')

    def get_success_url(self):
        return reverse_lazy('all_books')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)


class SingUp(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/sing_up.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('login')


