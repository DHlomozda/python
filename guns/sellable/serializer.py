from rest_framework import serializers
from .models import Sellable


class SellableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellable
        fields = '__all__'