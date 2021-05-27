from django.contrib import admin
from .models import Ticket,Supporter,ContactUs

admin.site.register(Ticket)
admin.site.register(Supporter)
admin.site.register(ContactUs)