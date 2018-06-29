from account.models import User,Group
from rest_framework import serializers, exceptions


class UserSerializer(serializers.ModelSerializer):
    uid = serializers.IntegerField()
    uname = serializers.CharField(max_length=20, default='')
    uqq = serializers.CharField(max_length=20, default='')
    password = serializers.CharField(max_length=200, default='')


    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ('password',)