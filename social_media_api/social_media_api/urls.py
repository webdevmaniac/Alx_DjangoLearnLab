
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
]



