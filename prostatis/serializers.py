from rest_framework import serializers
from prostatis.models import DayStatis,ProjectDayDetail



class DayStatisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayStatis
        fields = '__all__'


