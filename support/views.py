from django.contrib import messages
from django.http import request
from django.views.generic.edit import FormView
from support.forms import ContactUsForm,NewsletterForm
from .mixins import SupportRequiredMixin
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Ticket,ContactUs
from users.models import CustomUser

class AboutUs(FormView):
    template_name = "support/about_us.html"
    form_class = NewsletterForm
    success_url = "/"

    def form_valid(self,form):
        messages.success(self.request,"Successfully added to Newsletter")
        form.save(commit=False)
        email = form.cleaned_data.get("email")
        user = CustomUser.objects.get(email=email)
        user.newsletter = True
        user.save()
        form.save(commit=True)
        return super().form_valid(form)

class ContactUs(CreateView):
    model = ContactUs
    template_name = "support/contact_us.html"
    form_class = ContactUsForm
    success_url = "/landing/"

    def get_form_kwargs(self):
        kwargs = super(ContactUs, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class TicketListView(LoginRequiredMixin,ListView):
    model = Ticket
    template_name = 'support/ticket_list.html'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Ticket.objects.filter(creator=self.request.user)

    def get_context_data(self, *args,**kwargs):
        context = super(TicketListView,self).get_context_data(**kwargs)
        context["open"] = Ticket.objects.filter(creator=self.request.user,status=True)
        context["closed"] = Ticket.objects.filter(creator=self.request.user,status=False)    
        return context


class SupporterTicketListView(SupportRequiredMixin,LoginRequiredMixin,ListView):
    model = Ticket
    template_name = 'support/supporter_ticket_list.html'
    context_object_name = 'tickets'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Ticket.objects.filter(status=True,supporter__username=None or self.request.user.username)

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = "support/ticket_create.html"
    fields = ['title','content']
    success_url = "/support/tickets/"

    def form_valid(self, form):
        if not self.request.user.is_supporter:
            form.instance.creator = self.request.user
        return super().form_valid(form)

class TicketDetailView(LoginRequiredMixin,DetailView):
    model = Ticket
    template_name = "support/ticket_detail.html"
    context_object_name = "ticket"

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ['supporter','status']
    template_name = "support/ticket_update.html"

    def get_success_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_supporter:
            return True
        return False

class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = '/tickets/'
    template_name = "support/ticket_confirm_delete.html"

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.creator:
            return True
        return False