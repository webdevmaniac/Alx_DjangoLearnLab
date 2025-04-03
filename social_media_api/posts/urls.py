from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib import admin
from django.urls import include, path

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path("api/", include("posts.urls")),
]



