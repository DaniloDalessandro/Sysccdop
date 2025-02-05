from rest_framework import serializers
from .models import Direction,Management,Coordination

#===============================================================================

# Serializer direction
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'

#===============================================================================

# Serializer management
class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'

#================================================================================

# Serializer coordination
class CoordinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordination
        fields = '__all__'