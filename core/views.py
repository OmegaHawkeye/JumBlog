from support.forms import NewsletterForm
from django.http.response import HttpResponse
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
from .models import Article, Task
from django.db.models import Q
from bootstrap_datepicker_plus import DateTimePickerInput
from django.utils.safestring import mark_safe
import random

def handler404(request,exception):
    return render(request, 'error/404.html', {"exception":exception,"request":request}, status=404)
        
def handler500(request):
    return render(request, 'error/500.html', {"request":request}, status=500)

def LikeView(request,pk):
    if request.method == "POST":
        article = get_object_or_404(Article,id=pk)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
            article.save()
        else:
            article.likes.add(request.user)
            article.save()
        return HttpResponseRedirect(reverse("article-detail",args=[str(pk)]))
    return HttpResponse("Error. Access Denied")

def BookmarkView(request,pk):
    if request.method == "POST":
        article = get_object_or_404(Article,id=pk)
        if article.bookmarked:
            article.bookmarked = False
            article.save()
        else:
            article.bookmarked = True
            article.save()
        return HttpResponseRedirect(reverse("article-detail",args=[str(pk)]))
    return HttpResponse("Error. Access Denied")

def landing(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully added to Newsletter")
            return redirect("landing")    
    else:
        form = NewsletterForm()
    return render(request,"core/landing.html",{"form":form})

@login_required
def home(request):
    # first_article_id = Article.objects.first().id
    # last_article_id = Article.objects.last().id
    # random_Article_id = random.randrange(first_article_id,last_article_id)
    # random_Article = Article.objects.get(id=random_Article_id)
    first = Article.objects.filter(published=True).first()
    last = Article.objects.filter(published=True).last()
    triple = Article.objects.filter(published=True)[1:4]

    if(not request.user.first_name or not request.user.last_name):
       messages.info(request, mark_safe("Please complete your <a href='/accounts/profile'>Profile</a>! "))
    
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
    fields = ['image_thumbnail','title','subtitle','content','tags','category','published','allow_comments']
    success_url = "/articles/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = "article"
    fields = ['image_thumbnail','title','subtitle','content','tags','category','published','allow_comments']

    def get_context_data(self, *args,**kwargs):
        context = super(ArticleDetailView,self).get_context_data(**kwargs)
        article = get_object_or_404(Article,id=self.kwargs["pk"])
        liked = False
        bookmarked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        if article.bookmarked == True:
            bookmarked = True
        context["total_likes"] = article.total_likes
        context["liked"] = liked
        context["bookmarked"] = bookmarked
        return context

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['image_thumbnail','title','subtitle','content','tags','category','published','allow_comments']
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


class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    ordering = ['start']
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(completed=False)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_create.html"
    fields = ['name',"start","end"]
    success_url = "/tasks/"

    def get_form(self):
        form = super().get_form()
        form.fields["start"].widget = DateTimePickerInput()
        form.fields["end"].widget = DateTimePickerInput()
        return form

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['name',"start","end","completed"]
    template_name = "tasks/task_update.html"
    success_url = "/tasks/"

    def get_form(self):
        form = super().get_form()
        form.fields["start"].widget = DateTimePickerInput()
        form.fields["end"].widget = DateTimePickerInput()
        return form

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/tasks/'
    template_name = "tasks/task_confirm_delete.html"

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
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

