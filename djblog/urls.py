from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import blogs
from accounts.views import profile

app_name = 'djblog'
urlpatterns = [
    path('', blogs, name="blogs"),
    path('blogs/', include('blogs.urls'), name="blogs"),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('<str:username>/', profile, name='profile')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)