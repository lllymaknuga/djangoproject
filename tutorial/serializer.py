from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer, Serializer
from tutorial.models import Marker
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField


class MarkerSerializer(ModelSerializer):
    srid = serializers.IntegerField()
    # name = serializers.CharField()
    # list_of_choices = (('mw', 'men work'),  # дорожные работы
    #                    ('cr', 'crash'),  # Авария
    #                    ('cm', 'comment'),  # Комментарий
    #                    ('tc', 'temporary camera'),  # Временная камера
    #                    ('pc', 'pernament camers'),  # Постоянная камера
    #                    )
    # marker_type = serializers.ChoiceField(list_of_choices)

    location = PointField()

    class Meta:
        model = Marker
        fields = ['location', 'srid']

    def save(self, **kwargs):
        Marker.objects.create(location=Point(x=self.validated_data['location'][0],
                                             y=self.validated_data['location'][1],
                                             srid=self.validated_data['srid']))
