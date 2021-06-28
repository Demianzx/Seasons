from .serializers import DateToSeasons, SeasonsSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Order


class DateToSeasonsView(CreateAPIView):
    serializer_class = DateToSeasons
    
class GetSeasons(ListAPIView):
    serializer_class = SeasonsSerializer
    
    def get_queryset(self):
        return Order.objects.all()