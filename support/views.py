from .mixins import StaffRequiredMixin
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Ticket

class TicketListView(LoginRequiredMixin,ListView):
    model = Ticket
    template_name = 'ticket/ticket_list.html'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user)

    def get_context_data(self, *args,**kwargs):
        context = super(TicketListView,self).get_context_data(**kwargs)
        context["open"] = Ticket.objects.filter(creator=self.request.user,status="Open")
        context["closed"] = Ticket.objects.filter(creator=self.request.user,status="Closed")    
        return context


class SupporterTicketListView(StaffRequiredMixin,LoginRequiredMixin,ListView):
    model = Ticket
    template_name = 'ticket/supporter_ticket_list.html'
    context_object_name = 'tickets'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Ticket.objects.filter(supporter__user=self.request.user or None)

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = "ticket/ticket_create.html"
    fields = ['title','content']

    def get_success_url(self):
        return reverse('ticket-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TicketDetailView(LoginRequiredMixin,DetailView):
    model = Ticket
    template_name = "ticket/ticket_detail.html"
    context_object_name = "ticket"

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ['supporter','status']
    template_name = "ticket/ticket_update.html"

    def get_success_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = '/tickets/'
    template_name = "ticket/ticket_confirm_delete.html"

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.creator:
            return True
        return False