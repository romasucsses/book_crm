from django.urls import path
from .views import*

urlpatterns = [
    path('', Clients.as_view(), name='all_clients'),
    path('add_client/', AddClient.as_view(), name='add_client')

]