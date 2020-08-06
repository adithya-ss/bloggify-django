from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add another path for the django application home page.
    path('', include('blog_app.urls')),
    # Path to bloggers application.
    path('bloggers/', include('django.contrib.auth.urls')),
    path('bloggers/', include('bloggers.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
