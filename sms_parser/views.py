from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import SMSMessage
from .serializers import SMSMessageSerializer

from .utils.parser import (
    extract_amount,
    detect_merchant,
    is_subscription_message,
)

from subscriptions.models import Subscription


class SMSIngestView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        sender = request.data.get('sender')
        message = request.data.get('message')

        amount = extract_amount(message)

        merchant = detect_merchant(message)

        subscription_detected = is_subscription_message(message)

        sms = SMSMessage.objects.create(
            user=request.user,
            sender=sender,
            message=message,
            detected_merchant=merchant,
            detected_amount=amount,
            is_subscription=subscription_detected,
        )

        created_subscription = False

        if subscription_detected and merchant and amount:

            existing_subscription = Subscription.objects.filter(
                user=request.user,
                name=merchant,
                is_active=True
            ).first()

            if not existing_subscription:

                Subscription.objects.create(
                    user=request.user,
                    name=merchant,
                    amount=amount,
                    billing_cycle='monthly',
                    next_billing_date='2026-06-01',
                    category='Auto Detected',
                    source='sms',
                )

                created_subscription = True

        serializer = SMSMessageSerializer(sms)

        return Response({
            "sms": serializer.data,
            "subscription_created": created_subscription
        }, status=status.HTTP_201_CREATED)
