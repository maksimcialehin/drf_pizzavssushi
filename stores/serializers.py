from rest_framework import serializers
from .models import Pizzeria


class PizzeriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'logo_image',
            'restaurant_name',
            'street',
            'city',
        ]


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'logo_image',
            'restaurant_name',
            'street',
            'city',
            'website',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active',
        ]
