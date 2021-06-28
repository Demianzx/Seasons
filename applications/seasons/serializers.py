from rest_framework import serializers
from datetime import datetime, date
from .models import Order


class DateToSeasons(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    
class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pk','season')
    season = serializers.SerializerMethodField()

   

    def get_season(self, obj):
        Y = 2000
        seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
               ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
               ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
               ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
               ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]
        
        if isinstance(obj.ord_dt, datetime):
            now = obj.ord_dt.date()
        now = obj.ord_dt.replace(year=Y)
        return next(season for season, (start, end) in seasons
                    if start <= now <= end)