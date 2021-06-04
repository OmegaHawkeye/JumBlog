from django.test import TestCase
from django.contrib.auth.models import User
from django.urls.base import reverse
from support.models import Ticket,ContactUs


class Test_Ticket(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Omega",password="RexiSammy2003")
        self.ticket = Ticket.objects.create(title="Test1",content="Test1",creator=self.user,supporter=self.user)
        self.ticket1 = Ticket.objects.create(title="Test2",content="Test1",creator=self.user,supporter=self.user,status=False)
        
    def test_model(self):
        self.assertTrue(isinstance(self.ticket,Ticket))

    def test_str(self):
        self.assertEquals(str(self.ticket),"1 created by Omega and supported by Omega")

    def test_status_open(self):
        self.assertEquals(self.ticket.getStatus,"Open")
    
    def test_status_closed(self):
        self.assertEquals(self.ticket1.getStatus,"Closed")

    def test_get_absolute_url(self):
        url = reverse("ticket-detail",kwargs={"pk":1})
        self.assertEqual(url,self.ticket.get_absolute_url())


class Test_ContactUs(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username="Omega",email="chornitzerj@gmail.com",password="RexiSammy2003")
        self.contactus = ContactUs.objects.create(email=self.user.email,title="Test1",content="Test1")
        self.contactus1 = ContactUs.objects.create(email="chornitzerj@gmail.com",title="Test1",content="Test1")

    def test_model(self):
        self.assertTrue(isinstance(self.contactus,ContactUs))

    def test_str(self):
        self.assertEquals(str(self.contactus),"Test1 by chornitzerj@gmail.com")

