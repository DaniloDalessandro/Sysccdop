from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ContractInstallment, ContractAmendment, Contract
from .serializers import ContractInstallmentSerializer, ContractAmendmentSerializer, ContractSerializer
from .utils.exceptions import ContractAlreadyExists, ContractNotDeleted, InvalidContractData, ContractNotFound
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
        response.data['message'] = CONTRACTS_MESSAGES['CREATE_SUCCESS']
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

class ContractInstallmentListAPIView(generics.ListAPIView):
    queryset = ContractInstallment.objects.all()
    serializer_class = ContractInstallmentSerializer

#=======================================================================================================================

class ContractInstallmentCreateAPIView(generics.CreateAPIView):
    queryset = ContractInstallment.objects.all()
    serializer_class = ContractInstallmentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = CONTRACT_INSTALLMENTS_MESSAGES['CREATE_SUCCESS']
        return response

#=======================================================================================================================

class ContractInstallmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ContractInstallment.objects.all()
    serializer_class = ContractInstallmentSerializer

    def get_object(self):
        try:
            return ContractInstallment.objects.get(pk=self.kwargs['pk'])
        except ContractInstallment.DoesNotExist:
            raise ContractNotFound

#=======================================================================================================================

class ContractInstallmentUpdateAPIView(generics.UpdateAPIView):
    queryset = ContractInstallment.objects.all()
    serializer_class = ContractInstallmentSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = CONTRACT_INSTALLMENTS_MESSAGES['UPDATE_SUCCESS']
        return response

#=======================================================================================================================

class ContractInstallmentDestroyAPIView(generics.DestroyAPIView):
    queryset = ContractInstallment.objects.all()
    serializer_class = ContractInstallmentSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = CONTRACT_INSTALLMENTS_MESSAGES['DELETE_SUCCESS']
        return response

#=======================================================================================================================

class ContractAmendmentListAPIView(generics.ListAPIView):
    queryset = ContractAmendment.objects.all()
    serializer_class = ContractAmendmentSerializer

#=======================================================================================================================

class ContractAmendmentCreateAPIView(generics.CreateAPIView):
    queryset = ContractAmendment.objects.all()
    serializer_class = ContractAmendmentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = CONTRACT_AMENDMENTS_MESSAGES['CREATE_SUCCESS']
        return response

#=======================================================================================================================

class ContractAmendmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = ContractAmendment.objects.all()
    serializer_class = ContractAmendmentSerializer

    def get_object(self):
        try:
            return ContractAmendment.objects.get(pk=self.kwargs['pk'])
        except ContractAmendment.DoesNotExist:
            raise ContractNotFound

#=======================================================================================================================

class ContractAmendmentUpdateAPIView(generics.UpdateAPIView):
    queryset = ContractAmendment.objects.all()
    serializer_class = ContractAmendmentSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = CONTRACT_AMENDMENTS_MESSAGES['UPDATE_SUCCESS']
        return response

#=======================================================================================================================

class ContractAmendmentDestroyAPIView(generics.DestroyAPIView):
    queryset = ContractAmendment.objects.all()
    serializer_class = ContractAmendmentSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = CONTRACT_AMENDMENTS_MESSAGES['DELETE_SUCCESS']
        return response