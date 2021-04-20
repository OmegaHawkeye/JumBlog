from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Article


def home(request):
    first = Article.objects.first()
    last = Article.objects.last()
    triple = Article.objects.all()[1:4]
    return render(request,"core/home.html",{"first":first,"last":last,"triple":triple})


class ArticleListView(ListView,LoginRequiredMixin):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 5

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article/article_detail.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article/article_create.html"
    fields = ['title','content','image_url']
    success_url = "/articles/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title','content','image_url']
    template_name = "article/article_update.html"
    success_url = '/articles/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/articles/'
    template_name = "article/article_confirm_delete.html"

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False