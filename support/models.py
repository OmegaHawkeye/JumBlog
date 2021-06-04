from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from martor.models import MartorField

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = MartorField()
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    supporter = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ticket_supporter",blank=True,null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return f'{self.pk} created by {self.creator} and supported by {self.supporter}'

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})

    @property
    def getStatus(self):
        if self.status:
            return "Open"
        else:
            return "Closed"

class ContactUs(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=255)
    content = MartorField()

    class Meta: 
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f'{self.title} by {self.email}' 
