from rest_framework import serializers
from prostatis.models import ProjectDayStatis,DayStatis,UserStatis,UserDayStatis



class DayStatisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayStatis
        fields = '__all__'

class ProjectDayStatisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDayStatis
        fields = '__all__'

class UserDayStatisSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDayStatis
        fields = '__all__'


class UserStatisSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatis
        fields = '__all__'