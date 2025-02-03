from rest_framework import serializers

from .models import Assistance

class AidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = '__all__'