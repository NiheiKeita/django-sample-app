from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(created_by=user) | Task.objects.filter(
            assigned_to=user
        )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=["post"])
    def assign(self, request, pk=None):
        task = self.get_object()
        user_id = request.data.get("user_id")
        if user_id:
            task.assigned_to_id = user_id
            task.save()
            return Response(self.get_serializer(task).data)
        return Response({"error": "user_id is required"}, status=400)

    @action(detail=True, methods=["post"])
    def change_status(self, request, pk=None):
        task = self.get_object()
        status = request.data.get("status")
        if status in dict(Task.STATUS_CHOICES):
            task.status = status
            task.save()
            return Response(self.get_serializer(task).data)
        return Response({"error": "Invalid status"}, status=400)
