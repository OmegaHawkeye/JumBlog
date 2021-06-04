from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile


class Test_ContactUs(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username="Omega",email="chornitzerj@gmail.com",password="RexiSammy2003")
        self.user1 = User.objects.create(username="Chorn",email="omegahawkeye2@gmail.com",password="RexiSammy2003")
        self.user1.profile.newsletter = True

    def test_model(self):
        self.assertTrue(isinstance(self.user.profile,Profile))

    def test_str(self):
        self.assertEquals(str(self.user.profile),"Omega")

    def test_newsletter_off(self):
        self.assertEquals(self.user.profile.newsletter,False)

    def test_newsletter_on(self):
        self.assertEquals(self.user1.profile.newsletter,True)
    

