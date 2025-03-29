
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comments/new/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/comments/<int:comment_pk>/edit/', views.edit_comment, name='edit_comment'),
    path('post/<int:pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]



