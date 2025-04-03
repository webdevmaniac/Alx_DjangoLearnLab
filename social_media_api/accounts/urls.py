
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', views.FollowUserView.as_view()),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view()),
]


