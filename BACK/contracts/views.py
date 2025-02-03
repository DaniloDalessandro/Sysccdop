from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ContractInstallment, ContractAmendment, Contract
from .serializers import ContractInstallmentSerializer, ContractAmendmentSerializer, ContractSerializer
from .utils.exceptions import ContractAlreadyExists,ContractNotDeleted,InvalidContractData,ContractNotFound
from .utils.messages import CONTRACTS_MESSAGES, CONTRACT_INSTALLMENTS_MESSAGES, CONTRACT_AMENDMENTS_MESSAGES

class ContractListAPIView(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

#=======================================================================================================================

class ContractCreateAPIView(generics.CreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = "Contrato created successfully!"
        return response

#=======================================================================================================================

class ContractRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def get_object(self):
        try:
            return Contract.objects.get(pk=self.kwargs['pk'])
        except Contract.DoesNotExist:
            raise ContractNotFound

#=======================================================================================================================

class ContractUpdateAPIView(generics.UpdateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = CONTRACTS_MESSAGES['UPDATE_SUCCESS']
        return response

#=======================================================================================================================

class ContractDestroyAPIView(generics.DestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = CONTRACTS_MESSAGES['DELETE_SUCCESS']
        return response
        
#=======================================================================================================================


