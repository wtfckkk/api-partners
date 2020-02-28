from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from .models import Partner
import geojson


class PartnerSerializer(ModelSerializer):
    document = CharField(source='cnpj')

    class Meta:
        model = Partner
        exclude = ('cnpj',)

    def validate_address(self, address):
        if 'coordinates' in address:
            return geojson.Point(address['coordinates'])
        raise ValidationError("Needs coordinates")

    def validate_coverageArea(self, coverageArea):
        if 'coordinates' in coverageArea:
            return geojson.MultiPolygon(coverageArea['coordinates'])
        raise ValidationError("Needs coordinates")
