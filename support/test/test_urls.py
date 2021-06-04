from django.test import TestCase
from django.urls import reverse, resolve
from core.urls import *

class Test_Url(TestCase):
    
    def test_articlelistview_url_is_resolved(self):
        url = reverse("article-list")
        self.assertEquals(resolve(url).func.view_class,ArticleListView)

    def test_articledetailview_url_is_resolved(self):
        url = reverse("article-detail",args=[1])
        self.assertEquals(resolve(url).func.view_class,ArticleDetailView)