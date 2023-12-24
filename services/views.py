from django.db.models import F
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import Subscription
from services.serializers import SubscriptionSerializers


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.select_related("client", "client__user", "service", "plan"). \
        only("id", "plan_id", "client__company_name", "client__user__email", "service__full_price",
             "plan__discount_percent").\
        annotate(
        price=F("service__full_price") - F("service__full_price") * F("plan__discount_percent") / 100
    )
    serializer_class = SubscriptionSerializers
