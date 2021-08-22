from django.db import models
from django.urls import reverse
from django.db import models
from tinymce.models import HTMLField
from django_project.settings import AUTH_USER_MODEL

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    creator = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    supporter = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="ticket_supporter",blank=True,null=True)
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
    content = HTMLField()

    class Meta: 
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f'{self.title} by {self.email}' 

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.email