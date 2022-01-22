import json
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from tutorial.models import Marker
from tutorial.serializer import MarkerSerializer, MarkerListSerializer


class MarkerViewPost(APIView):
    serializer_class = MarkerSerializer

    def post(self, request):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)
        Marker.objects.create(location=Point(x=ser.validated_data['latitude'], y=ser.validated_data['longitude']),
                              name=ser.validated_data['name'], marker_type=ser.validated_data['marker_type'])
        return Response(status=status.HTTP_200_OK)


def gt_queryset():
    return Marker.objects.all()


class MarkerViewGet(ListAPIView):
    serializer_class = MarkerListSerializer
    queryset = gt_queryset()
