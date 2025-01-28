from rest_framework import serializers
from .models import Management_Center,Requesting_Center


# Serializer for the models in the centers app
class ManagementCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management_Center
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


# Serializer for the models in the centers app
class RequestingCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requesting_Center
        fields = ['id','management_center', 'name', 'description', 'created_at', 'updated_at']