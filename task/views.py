from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer,UserSerializer
from .filters import TaskFilter
from .permissions import PostOnly


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TaskFilter
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user, archived=False)
        return Task.objects.none()
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

        
class RegisterViewSet(ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = [PostOnly]