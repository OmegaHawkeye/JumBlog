from django import forms 
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

    def __init__(self,*args, **kwargs):
        self.user = kwargs.pop('user')
        super(ContactUsForm, self).__init__(*args, **kwargs)
        if self.user.is_authenticated:
            self.initial['email'] = self.user.email