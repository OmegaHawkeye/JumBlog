from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django_comments_xtd.models import XtdComment

class Supporter(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

STATUS_CHOICES = (
    ("Open","OPEN"),
    ("Closed","CLOSED")
)

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    supporter = models.ForeignKey(Supporter,on_delete=models.CASCADE,related_name="ticket_supporter",blank=True,null=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default="Open")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return f'{self.pk} created by {self.creator} and supported by {self.supporter}'

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})