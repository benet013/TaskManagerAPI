import django_filters
from django.utils import timezone
from .models import Task

class TaskFilter(django_filters.FilterSet):
    overdue = django_filters.BooleanFilter(method='filter_overdue',label='Overdue Tasks')
    
    class Meta:
        model = Task
        fields = {
            'completed' : ['exact'],
            'priority' : ['exact']
        }
        
    def filter_overdue(self, queryset, name ,value):
        if value:
            return queryset.filter(due_date__lt=timezone.now(), completed=False)
        return queryset
    