from rest_framework import serializers
from .models import Direction,Management,Coordination

# Serializer direction
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

#===============================================================================

# Serializer management
class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ['id', 'direction','name', 'description', 'created_at', 'updated_at']

#================================================================================

# Serializer coordination
class CoordinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordination
        fields = ['id','management','name', 'description', 'created_at', 'updated_at']