from .models import UserQuery
from rest_framework import serializers


class UserQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuery
        fields = ['id', 'user', 'user_query']
        