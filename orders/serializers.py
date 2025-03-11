from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order  # Connects to order model
        fields = '__all__'  # Includes all fields
