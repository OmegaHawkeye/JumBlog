from django.urls import path
from .views import *

urlpatterns = [
    path("",landing,name="landing"),
    path("home/",home,name="home"),
    path("search/", SearchResultView.as_view(), name="search"),
    path("articles/bookmarked",BookmarkedArticleListView.as_view(),name="bookmarked-article-list"),
    path("articles/categorized/<str:category>/",CategoryListView.as_view(),name="categorized-article-list"),
    path("articles/user/",UserArticleListView.as_view(),name="user-articles-list"),
    path("articles/published/<str:username>/",PublishedArticleListView.as_view(),name="user-published-articles-list"),
    path("articles/drafted/",DraftedArticleListView.as_view(),name="drafted-articles-list"),
    path("articles/",ArticleListView.as_view(),name="article-list"),
    path("article/create/",ArticleCreateView.as_view(),name="article-create"),
    path("article/<int:pk>/detail/",ArticleDetailView.as_view(),name="article-detail"),
    path("article/<int:pk>/update/",ArticleUpdateView.as_view(),name="article-update"),
    path("article/<int:pk>/delete/",ArticleDeleteView.as_view(),name="article-delete"),
    path("bookmark/<int:pk>/",BookmarkView,name="bookmark-article"),
    path("like/<int:pk>/",LikeView,name="like-article"),
    path("create/article/",CreateArticle.as_view(),name="create-article"),
    
]