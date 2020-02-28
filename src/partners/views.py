from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import PartnerSerializer
from .utils.nearest_partner import get_nearest_partner
from .models import Partner


class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    @action(methods=['post'], detail=False)
    def nearest(self, request):
        nearest_partner_id = get_nearest_partner(Partner.objects.all(), request.data['coordinates'])
        instance = Partner.objects.get(id=nearest_partner_id)
        serializer = PartnerSerializer(instance)
        return Response(serializer.data)
