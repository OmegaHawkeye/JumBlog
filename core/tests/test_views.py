# from django.test import TestCase
# from django.test.client import Client
# from django.urls import reverse

# class Testviews(TestCase):
    
#     def setUp(self):
#         self.client = Client()
#         self.article_list_url = reverse("article-list")
#         #self.article_detail_url = reverse("article-detail",args=[1])

#     def test_article_list_GET(self):
#         response = self.client.get(self.article_list_url)

#         self.assertEquals(response.status_code,302)
#         self.assertTemplateUsed(response,"article/article_list.html")
#         print(response.templates)