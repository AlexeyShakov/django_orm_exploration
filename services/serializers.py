from rest_framework import serializers

from .models import Subscription, Plan, Service


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ("id", "discount_percent")


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "full_price")


class SubscriptionSerializers(serializers.ModelSerializer):
    plan = PlanSerializer()
    service = ServiceSerializer()
    client_name = serializers.CharField(source="client.company_name")
    email = serializers.CharField(source="client.user.email")
    price = serializers.SerializerMethodField()

    def get_price(self, instance: Subscription):
        return instance.price

    class Meta:
        model = Subscription
        fields = ("id", "plan_id", "client_name", "email", "price", "plan", "service")
