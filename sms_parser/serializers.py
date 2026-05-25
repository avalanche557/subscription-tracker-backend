from rest_framework import serializers
from .models import SMSMessage


class SMSMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SMSMessage

        fields = '__all__'

        read_only_fields = [
            'user',
            'detected_merchant',
            'detected_amount',
            'is_subscription',
        ]