from rest_framework import serializers
from prostatis.models import DayStatis



class DayStatisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayStatis
        fields = '__all__'


