from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from books.models import Book
from clients.models import Client
from orders.models import Order
from mixins.mixin_global import CurrentPageContext
from orders.forms import AddOrderForm


class Orders(CurrentPageContext, ListView):
    model = Order
    template_name = 'orders/orders.html'
    context_object_name = 'all_orders'
    # mixin info
    mixin_page_name = 'all_orders'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            orders = Order.objects.filter(pk=query)
        else:
            orders = Order.objects.all()
        return orders


class OrderPost(CurrentPageContext, DetailView):
    model = Order
    template_name = "orders/order_post.html"
    context_object_name = 'orders'
    pk_url_kwarg = 'pk_order'
    # mixin info
    mixin_page_name = 'order_post'

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.kwargs['pk_order'])

    def get_post(self):
        return get_object_or_404(self.get_queryset())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.object
        customers = get_object_or_404(Client, order=order)
        books = get_object_or_404(Book, order=order)
        context['books'] = books
        context['customers'] = customers

        return context


class AddOrder(CreateView):
    form_class = AddOrderForm
    template_name = 'orders/add_order.html'
    success_url = reverse_lazy('all_orders')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customers = Client.objects.all()
        books = Book.objects.all()
        all_orders = Order.STATUS_CHOICES
        context['books'] = books
        context['customers'] = customers
        context['all_orders'] = all_orders

        return context
