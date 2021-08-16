from django.contrib import admin
from .models import Ticket,ContactUs,Newsletter

admin.site.register(Ticket)
admin.site.register(ContactUs)
admin.site.register(Newsletter)