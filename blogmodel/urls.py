from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('search', views.search, name = "search"),
    path('new', views.new, name = "new"),
    path('create', views.create, name="create"),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('update/<int:post_id>', views.edit, name="update"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
