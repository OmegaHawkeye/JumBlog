from django.test import TestCase
from users.models import CustomUser

class Test_ContactUs(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create(username="Omega",email="chornitzerj@gmail.com",password="RexiSammy2003")
        self.user1 = CustomUser.objects.create(username="Chorn",email="omegahawkeye2@gmail.com",password="RexiSammy2003")
        self.user1.newsletter = True

    def test_model(self):
        self.assertTrue(isinstance(self.user,CustomUser))

    def test_newsletter_off(self):
        self.assertEquals(self.user.newsletter,False)

    def test_newsletter_on(self):
        self.assertEquals(self.user1.newsletter,True)
    

