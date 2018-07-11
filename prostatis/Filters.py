import django_filters
from project.models import ProjectInvestDataModel
from prostatis.models import  ProjectDayStatis,UserDayStatis,DayStatis,UserStatis


class ProjectInvestDataFilter(django_filters.rest_framework.FilterSet):
    investtime = django_filters.DateFromToRangeFilter(name="invest_time")
    audittime = django_filters.DateTimeFromToRangeFilter(name="audit_time")
    projectname = django_filters.CharFilter(name="project", lookup_expr='name__contains')
    class Meta:
        model = ProjectInvestDataModel
        fields = ['is_futou', 'invest_time', 'project', 'projectname', 'investtime','state', 'invest_mobile', 'audittime', 'source']

class ProjectDayStatisFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = ProjectDayStatis
        fields = '__all__'

class UserDayStatisFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = UserDayStatis
        fields = '__all__'

class DayStatisFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = DayStatis
        fields = '__all__'

class UserStatisFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = UserStatis
        fields = '__all__'