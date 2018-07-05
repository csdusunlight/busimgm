import django_filters
from project.models import Project,FundApplyLog,RefundApplyLog,InvoiceApplyLog,OperatorLog
class ProjectFilter(django_filters.rest_framework.FilterSet):
    lanched_apply_date = django_filters.DateFromToRangeFilter(name="lanched_apply_date")
    lanched_audit_date = django_filters.DateFromToRangeFilter(name="lanched_audit_date")
    concluded_apply_date = django_filters.DateFromToRangeFilter(name="concluded_apply_date")
    concluded_audit_date = django_filters.DateFromToRangeFilter(name="concluded_audit_date")
    name = django_filters.CharFilter(name="name", lookup_expr='contains')
    platname = django_filters.CharFilter(name="platname", lookup_expr='contains')
    class Meta:
        model = Project
        fields = ['id', 'platname', 'name','state', 'contact', 'settleway',
                  'contract_company','lanched_apply_date','lanched_audit_date','concluded_apply_date','concluded_audit_date']

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


class OperatorLogFilter(django_filters.rest_framework.FilterSet):
    apply_date = django_filters.DateFromToRangeFilter(name="apply_date")
    audit_date = django_filters.DateFromToRangeFilter(name="audit_date")
    audit_state = django_filters.CharFilter(name="audit_state", lookup_expr='contains')
    class Meta:
        model = OperatorLog
        fields = "__all__"
