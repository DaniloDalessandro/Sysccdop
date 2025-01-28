from rest_framework import serializers
from .models import Management_Center

class ManagementCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management_Center
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
