import django_filters
from project.models import Project
class ProjectFilter(django_filters.rest_framework.FilterSet):
    startDate = django_filters.DateFromToRangeFilter(name="time")
    finishdate = django_filters.DateFromToRangeFilter(name="finish_time")
    name = django_filters.CharFilter(name="name", lookup_expr='contains')
    platform = django_filters.CharFilter(name="platform", lookup_expr='contains')
    class Meta:
        model = Project
        fields = ['id', 'platform', 'name', 'startDate','state', 'contact', 'settleway',
                  'contract_company','finishdate']