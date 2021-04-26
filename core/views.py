
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# from gtts import gTTS
from django.utils.safestring import mark_safe,SafeString
from .models import Article
from users.models import Profile
import random

def get_xp(request):
    first_article_id = Article.objects.first().id
    last_article_id = Article.objects.last().id
    random_Article_id = random.randrange(first_article_id,last_article_id)
    random_Article = Article.objects.get(id=random_Article_id)
    if request.method == 'POST':
        curr_prof = Profile.objects.get(user=request.user)
        curr_prof.xp += random_Article.gained_xp
        curr_prof.save()
        # text = random_Article.content
        # save_text = mark_safe(text)
        # my_obj = gTTS(text=text,lang="en",slow=False)
        # my_obj.save("speech.mp3")
    return render(request,"core/get_xp.html",{"random_article":random_Article,"user_xp":request.user.profile.xp})

def home(request):
    first = Article.objects.first()
    last = Article.objects.last()
    triple = Article.objects.all()[1:4]
    return render(request,"core/home.html",{"first":first,"last":last,"triple":triple})

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = 'articles'
    ordering = ['-needed_xp']
    paginate_by = 5

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article/article_detail.html"
    context_object_name = "article"

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article/article_create.html"
    fields = ['title','content','needed_xp','gained_xp','image_url']
    success_url = "/articles/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title','content','needed_xp','gained_xp','image_url']
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

    