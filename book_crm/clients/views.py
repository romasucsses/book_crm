from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from clients.forms import AddClientForm
from clients.models import Client
from mixins.mixin_global import CurrentPageContext


class Clients(CurrentPageContext, ListView):
    model = Client
    template_name = 'clients/clients.html'
    context_object_name = 'all_clients'
    ordering = 'pk'
    paginate_by = 6

    # mixin info
    mixin_page_name = 'all_clients'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_clients_numb'] = str(Client.objects.count())
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            clients = Client.objects.filter(pk=query)
        else:
            clients = Client.objects.all()
        return clients


class AddClient(CreateView):
    form_class = AddClientForm
    template_name = 'clients/add_client.html'
    success_url = reverse_lazy('all_clients')