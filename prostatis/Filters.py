import django_filters
from prostatis.models import  ProjectInvestData


class ProjectInvestDataFilter(django_filters.rest_framework.FilterSet):
    investtime = django_filters.DateFromToRangeFilter(name="invest_time")
    audittime = django_filters.DateTimeFromToRangeFilter(name="audit_time")
    projectname = django_filters.CharFilter(name="project", lookup_expr='name__contains')
    class Meta:
        model = ProjectInvestData
        fields = ['is_futou', 'invest_time', 'project', 'projectname', 'investtime','state', 'invest_mobile', 'audittime', 'source']
