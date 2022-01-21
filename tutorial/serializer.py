from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer, Serializer
from tutorial.models import Marker
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField


class MarkerSerializer(Serializer):
    latitude = serializers.FloatField()  # широта
    longitude = serializers.FloatField()  # долгота
    name = serializers.CharField()
    list_of_choices = (('mw', 'men work'),  # дорожные работы
                       ('cr', 'crash'),  # Авария
                       ('cm', 'comment'),  # Комментарий
                       ('tc', 'temporary camera'),  # Временная камера
                       ('pc', 'pernament camers'),  # Постоянная камера
                       )
    marker_type = serializers.ChoiceField(list_of_choices)


class MarkerListSerializer(ModelSerializer):
    class Meta:
        model = Marker
        fields = '__all__'
