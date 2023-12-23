from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import Subscription
from services.serializers import SubscriptionSerializers


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.select_related("client", "client__user").only("id", "plan_id", "client__company_name", "client__user__email")
    serializer_class = SubscriptionSerializers
