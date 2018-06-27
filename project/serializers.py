from rest_framework import serializers
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    state_des = serializers.CharField(source='get_state_display', read_only=True)
    settleway_des = serializers.CharField(source='get_settleway_display', read_only=True)
    platformname = serializers.CharField(source='platform', read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id','settleway_des','consume','state_des', 'time')