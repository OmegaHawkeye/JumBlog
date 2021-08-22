from django.test import TestCase
from users.models import CustomUser
from django.urls.base import reverse
from core.models import Article,Task
import datetime

class Test_Article(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create(username="Omega",password="RexiSammy2003")
        self.article = Article.objects.create(title="Test1",author=self.user,content="Test1")
        self.article1 = Article.objects.create(title="Test2",author=self.user,content="Test1",published=False)

    def test_model(self):
        self.assertTrue(isinstance(self.article,Article))
  
    def test_str(self):
        self.assertEquals(str(self.article),"Test1 created by Omega")

    def test_status_published(self):
        self.assertEquals(self.article.status,"Published")

    def test_status_drafted(self):
        self.assertEquals(self.article1.status,"Drafted")

    def test_likes_counter(self):
        self.assertEquals(self.article.total_likes,0)

    def test_get_absolute_url(self):
        url = reverse("article-detail",kwargs={"pk":1})
        self.assertEqual(url,self.article.get_absolute_url())

class Test_Task(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="Omega",password="RexiSammy2003")
        self.task = Task.objects.create(name="Test1",creator=self.user,start=datetime.datetime.now(),end=datetime.datetime(2021, 8, 4, 15, 24))
        self.task1 = Task.objects.create(name="Test2",creator=self.user,start=datetime.datetime.now(),end=(datetime.datetime.now() + datetime.timedelta(days=5)))
        self.task2 = Task.objects.create(name="Test3",creator=self.user,start=datetime.datetime.now(),end=datetime.datetime.now(),completed=True)

    def test_model(self):
        self.assertTrue(isinstance(self.task,Task))

    def test_str(self):
        self.assertEquals(str(self.task),"Test1 created by Omega")

    def test_status_uncompleted(self):
        self.assertEquals(self.task.getStatus,"Uncompleted")

    def test_status_outdated(self):
        self.assertEquals(self.task1.getStatus,"Outdated")

    def test_status_completed(self):
        self.assertEquals(self.task2.getStatus,"Completed")

    def test_get_absolute_url(self):
        url = reverse("task-detail",kwargs={"pk":1})
        self.assertEqual(url,self.task.get_absolute_url())