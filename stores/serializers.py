from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Pizzeria


class PizzeriaListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'logo_image',
            'restaurant_name',
            'street',
            'city',
            'absolute_url',
        ]

    def get_absolute_url(self, obj):
        return reverse('pizzeria_detail', args=(obj.pk,))


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()
    
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'logo_image',
            'restaurant_name',
            'street',
            'city',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active',
            'update',
            'delete',
        ]

    def get_update(self, obj):
        return reverse('pizzeria_update', args=(obj.pk,))

    def get_delete(self, obj):
        return reverse('pizzeria_delete', args=(obj.pk,))
