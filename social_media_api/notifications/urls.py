from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.GetNotificationsView.as_view()),
    path('notifications/create/', views.CreateNotificationView.as_view()),
]
