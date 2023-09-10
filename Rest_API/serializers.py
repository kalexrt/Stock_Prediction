from rest_framework import serializers
from .models import DataStock

class DataStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataStock
        fields = ['Symbol', 'Date','Open', 'High', 'Low', 'Close', 'Vol']

