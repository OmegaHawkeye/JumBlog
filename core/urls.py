from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    
    path("articles/",ArticleListView.as_view(),name="article-list"),
    path("article/create/",ArticleCreateView.as_view(),name="article-detail"),
    path("article/<int:pk>/detail/",ArticleDetailView.as_view(),name="article-detail"),
    path("article/<int:pk>/update/",ArticleUpdateView.as_view(),name="article-update"),
    path("article/<int:pk>/delete/",ArticleDeleteView.as_view(),name="article-delete"),
]