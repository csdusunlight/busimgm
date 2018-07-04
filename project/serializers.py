from rest_framework import serializers
from project.models import Project,FundApplyLog,RefundApplyLog,InvoiceApplyLog

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
    #project = serializers.CharField(source="project.id",read_only=True)
    class Meta:
        model = FundApplyLog
        fields = '__all__'

class  FundApplyLogListSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source="project.id",read_only=True)
    class Meta:
        model = FundApplyLog
        fields = '__all__'


class  RefundApplyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefundApplyLog
        fields = '__all__'


class  RefundApplyLogListSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source="project.id", read_only=True)
    class Meta:
        model = RefundApplyLog
        fields = '__all__'

class  InvoiceApplyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceApplyLog
        fields = '__all__'

class  InvoiceApplyLogListSerializer(serializers.ModelSerializer):
    project = serializers.CharField(source="project.id", read_only=True)
    class Meta:
        model = InvoiceApplyLog
        fields = '__all__'
