from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer

class CreateNotificationView(APIView):
    def post(self, request):
        notification = Notification.objects.create(
            recipient=request.user,
            actor=request.user,
            verb=request.data['verb'],
            target_content_type_id=request.data['target_content_type_id'],
            target_object_id=request.data['target_object_id']
        )
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetNotificationsView(APIView):
    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
