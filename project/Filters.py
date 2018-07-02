import django_filters
from project.models import Project,FundApplyLog
class ProjectFilter(django_filters.rest_framework.FilterSet):
    startDate = django_filters.DateFromToRangeFilter(name="lanched_date")
    finishdate = django_filters.DateFromToRangeFilter(name="concluded_date")
    name = django_filters.CharFilter(name="name", lookup_expr='contains')
    platname = django_filters.CharFilter(name="platname", lookup_expr='contains')
    class Meta:
        model = Project
        fields = ['id', 'platname', 'name', 'startDate','state', 'contact', 'settleway',
                  'contract_company','concluded_date']

class FundApplyLogFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = FundApplyLog
        fields = "__all__"

