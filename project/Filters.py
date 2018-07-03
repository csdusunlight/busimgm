import django_filters
from project.models import Project,FundApplyLog,RefundApplyLog,InvoiceApplyLog
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
    apply_date = django_filters.DateFromToRangeFilter(name="apply_date")
    audit_date = django_filters.DateFromToRangeFilter(name="audit_date")
    audit_state = django_filters.CharFilter(name="audit_state", lookup_expr='contains')


    class Meta:
        model = FundApplyLog
        fields = "__all__"

class RefundApplyLogFilter(django_filters.rest_framework.FilterSet):
    apply_date = django_filters.DateFromToRangeFilter(name="apply_date")
    audit_date = django_filters.DateFromToRangeFilter(name="audit_date")
    audit_state = django_filters.CharFilter(name="audit_state", lookup_expr='contains')
    class Meta:
        model = RefundApplyLog
        fields = "__all__"

class InvoiceApplyLogFilter(django_filters.rest_framework.FilterSet):
    apply_date = django_filters.DateFromToRangeFilter(name="apply_date")
    audit_date = django_filters.DateFromToRangeFilter(name="audit_date")
    audit_state = django_filters.CharFilter(name="audit_state", lookup_expr='contains')
    class Meta:
        model = InvoiceApplyLog
        fields = "__all__"
