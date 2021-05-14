from django.urls import path
from .views import *

urlpatterns = [
    
    path("tickets/",TicketListView.as_view(),name="ticket-list"),
    path("ticket/create/",TicketCreateView.as_view(),name="ticket-create"),
    path("ticket/<int:pk>/detail/",TicketDetailView.as_view(),name="ticket-detail"),
    path("ticket/<int:pk>/update/",TicketUpdateView.as_view(),name="ticket-update"),
    path("ticket/<int:pk>/delete/",TicketDeleteView.as_view(),name="ticket-delete"),

    path("tickets/supporter",SupporterTicketListView.as_view(),name="supporter-ticket-list"),
]