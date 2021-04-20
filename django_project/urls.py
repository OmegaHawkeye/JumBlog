from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_email_verification import urls as email_urls
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('users.urls')),
    path('email/', include(email_urls)),
    path('', include('core.urls')),
    path('accounts/', include('allauth.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
