from .models import Budget, BudgetMovement
from rest_framework import serializers

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class BudgetMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetMovement
        fields = '__all__'