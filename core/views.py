from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article
from django.db.models import Q

def handler404(request,exception):
    return render(request, 'error/404.html', {"exception":exception,"request":request}, status=404)

    
def handler500(request):
    return render(request, 'error/500.html', {"request":request}, status=500)

def LikeView(request,pk):
    article = get_object_or_404(Article,id=request.POST.get("article_id"))
    if article.liked.filter(id=request.user.id).exists():
        article.liked.remove(request.user)
        liked=False
    else:
        article.liked.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse("article-detail",args=[str(pk)]))

def BookmarkView(request,pk):
    article = get_object_or_404(Article,id=request.POST.get("article_id"))
    if article.bookmarked == True:
        article.bookmarked = False
        article.save()
        bookmarked = False
    else:
        article.bookmarked = True
        article.save()
        bookmarked = True
    return HttpResponseRedirect(reverse("article-detail",args=[str(pk)]))

def landing(request):
    if request.user.is_authenticated:
        messages.success(request, f'''You have been redirected since your already logged in''')
        return redirect("home")
    return render(request,"core/landing.html")

@login_required
def home(request):
    first = Article.objects.filter(published=True).first()
    last = Article.objects.filter(published=True).last()
    triple = Article.objects.filter(published=True)[1:4]
    
    return render(request,"core/home.html",{"first":first,"last":last,"triple":triple})

class BookmarkedArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/bookmarked_article_list.html'
    context_object_name = 'bookmarked_articles'
    ordering = ['-created_at']

    def get_queryset(self):
        return Article.objects.filter(bookmarked=True)

class CategoryListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/categorized_article_list.html'
    context_object_name = 'categorized_articles'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(category=self.kwargs.get("category"))

class DraftedArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/drafted_article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user,published=False)

class PublishedArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/published_article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(author__username=self.kwargs.get("username"),published=True)

class UserArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/user_article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(published=True)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article/article_create.html"
    fields = ['image','title','subtitle','content','tags','category','published','allow_comments']
    success_url = "/articles/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = "article"
    fields = ['image','title','subtitle','content','tags','category','published','allow_comments']

    def get_context_data(self, *args,**kwargs):
        context = super(ArticleDetailView,self).get_context_data(**kwargs)
        article = get_object_or_404(Article,id=self.kwargs["pk"])
        liked = False
        if article.liked.filter(id=self.request.user.id).exists():
            liked = True
        bookmarked = False
        if article.bookmarked == True:
            bookmarked = True
        context["liked"] = liked
        context["bookmarked"] = bookmarked
        return context

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['image','title','subtitle','content','tags','category','published','allow_comments']
    template_name = "article/article_update.html"
    # success_url = '/articles/'

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.id})

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

class SearchResultView(ListView):
    model = Article
    template_name = "article/search-info.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Article.objects.filter(
            Q(title__icontains=query) |
            Q(subtitle__icontains=query) |
            Q(author__username__icontains=query) |
            Q(content__icontains=query) |
            Q(category__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
        return object_list


class CreateArticle(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "article/writeArticle.html"
    fields = ['image','title','subtitle','content','category','tags']
    success_url = "/articles/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


