from django import forms 
from .models import ContactUs,Newsletter

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

    def __init__(self,*args, **kwargs):
        self.user = kwargs.pop('user')
        super(ContactUsForm, self).__init__(*args, **kwargs)
        if self.user.is_authenticated:
            self.initial['email'] = self.user.email

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]
    
    def __init__(self,*args, **kwargs):
        super(NewsletterForm,self).__init__(*args,**kwargs)
        self.fields["email"].widget.attrs['class'] = 'form-control'
        self.fields["email"].label = ""
        self.fields["email"].widget.attrs["placeholder"] = "Your Email"
