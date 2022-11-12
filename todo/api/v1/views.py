from rest_framework import viewsets, filters
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from todo.models import Task
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["id", "title", "user"]
    search_fields = ["user", "id", "title"]


class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = "id"

