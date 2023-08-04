from django.urls import path
from .views import*
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('register/', SingUp.as_view(), name='singup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]