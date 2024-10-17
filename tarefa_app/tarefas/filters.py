# tarefas/filters.py

import django_filters
from .models import TimeEntry

class TimeEntryFilter(django_filters.FilterSet):
    data_registro = django_filters.DateFromToRangeFilter()
    duracao = django_filters.DurationFilter()
    descricao = django_filters.CharFilter(lookup_expr='icontains')
    task__descricao = django_filters.CharFilter(lookup_expr='icontains', label='Tarefa')

    class Meta:
        model = TimeEntry
        fields = ['data_registro', 'duracao', 'descricao', 'task__descricao']
