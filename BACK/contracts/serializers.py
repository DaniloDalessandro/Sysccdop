from rest_framework import serializers
from .models import Contract,ContractAmendment,ContractInstallment

class ContractSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Contract
        fields = '__all__'

class ContractAmendmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractAmendment
        fields = '__all__'

class ContractInstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractInstallment
        fields = '__all__'