from rest_framework import serializers

from .models import Aid

class AidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aid
        fields = '__all__'