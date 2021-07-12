from django.test import TestCase
<<<<<<< HEAD
from django.urls import reverse, resolve
from core.urls import *

class Test_Url(TestCase):
    
    def test_articlelistview_url_is_resolved(self):
        url = reverse("article-list")
        self.assertEquals(resolve(url).func.view_class,ArticleListView)

    def test_articledetailview_url_is_resolved(self):
        url = reverse("article-detail",args=[1])
        self.assertEquals(resolve(url).func.view_class,ArticleDetailView)
=======
from core.views import *
from django.urls import reverse,resolve

class TestUrls(TestCase):

    def test_article_list_url_resolves(self):
        url = reverse("article-list")
        self.assertEquals()resolve(url).func.view_class,ArticleListView)
    
    def test_article_create_url_resolves(self):
        url = reverse("article-create")
        self.assertEquals()resolve(url).func.view_class,ArticleCreateView)
        
    def test_article_detail_url_resolves(self):
        url = reverse("article-detail",args=[1])
        self.assertEquals()resolve(url).func.view_class,ArticleDetailView)
    
    def test_article_update_url_resolves(self):
        url = reverse("article-update",args=[1])
        self.assertEquals()resolve(url).func.view_class,ArticleUpdateView)
        
    def test_article_delete_url_resolves(self):
        url = reverse("article-delete")
        self.assertEquals()resolve(url).func.view_class,ArticleDeleteView)
        
    def test_landing_url_resolves(self):
        url= reverse("landing")
        self.assertEquals(resolve(url).func,landing)
    

    def test_home_url_resolves(self):
        url= reverse("home")
        self.assertEquals(resolve(url).func,home)
    
>>>>>>> a43a53a2dcc6160483e9c9e33d36069469f53cba