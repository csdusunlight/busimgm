from rest_framework import serializers
from project.models import Project,FundApplyLog

class ProjectSerializer(serializers.ModelSerializer):
    state_des = serializers.CharField(source='get_state_display', read_only=True)
    settleway_des = serializers.CharField(source='get_settleway_display', read_only=True)
    platformname = serializers.CharField(source='platform', read_only=True)
    profit = serializers.DecimalField(decimal_places=2,max_digits=10,read_only=True)
    topay_amount= serializers.DecimalField(decimal_places=2,max_digits=10,read_only=True)
    #contact = serializers.CharField(source="contact.uname",read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id','settleway_des','consume','state_des', 'time','profit','topay_amount')

class  FundApplyLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = FundApplyLog
        fields = '__all__'


class  FundApplyLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = FundApplyLog
        fields = '__all__'


