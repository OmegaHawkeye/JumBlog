from django.contrib.sitemaps import Sitemap
from .models import Article

class ArticleViewSitemap(Sitemap):
    changefreq = "always"
    priority = 1.0

    def items(self):
        return Article.objects.all()

    def lastmod(self,obj):
        return obj.updated_at