from django.urls import path
from .views import*

urlpatterns = [
    path('', Orders.as_view(), name='all_orders'),
    path('<int:pk_order>/', OrderPost.as_view(), name='order_post'),
    path('add_order/', AddOrder.as_view(), name='add_order')

]