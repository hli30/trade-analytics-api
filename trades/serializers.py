from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.conf import settings

from .models import History
from users.models import Account

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        exclude = ('user_id',)

    def create(self, validated_data):
        validated_data['user_id'] = Account.objects.get(pk=validated_data['user_id'])
        return History.objects.create(**validated_data)

    