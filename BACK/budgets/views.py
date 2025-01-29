from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .models import Budget
from .serializers import BudgetSerializer
from .utils.exceptions import BudgetNotFound, InvalidBudgetData, BudgetAlreadyExists, InvalidBudgetStatus
from .utils.messages import BUDGETS_MESSAGES

#===============================================================================
class BudgetsListAPIView(generics.ListAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

#===============================================================================

class BudgetCreateAPIView(generics.CreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except InvalidBudgetData:
            raise InvalidBudgetData(BUDGETS_MESSAGES['INVALID_DATA'])
        except BudgetAlreadyExists:
            raise BudgetAlreadyExists(BUDGETS_MESSAGES['ALREADY_EXISTS'])

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = BUDGETS_MESSAGES['CREATE_SUCCESS']
        return response

#===============================================================================

class BudgetRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_object(self):
        try:
            return Budget.objects.get(pk=self.kwargs['pk'])
        except Budget.DoesNotExist:
            raise BudgetNotFound

#===============================================================================

class BudgetUpdateAPIView(generics.UpdateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_update(self, serializer):
        try:
            serializer.save()
        except InvalidBudgetData:
            raise InvalidBudgetData(BUDGETS_MESSAGES['INVALID_DATA'])
        except BudgetAlreadyExists:
            raise BudgetAlreadyExists(BUDGETS_MESSAGES['ALREADY_EXISTS'])
        except InvalidBudgetStatus:
            raise InvalidBudgetStatus(BUDGETS_MESSAGES['INVALID_STATUS'])

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = BUDGETS_MESSAGES['UPDATE_SUCCESS']
        return response

#===============================================================================

class BudgetDestroyAPIView(generics.DestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except BudgetNotFound:
            raise BudgetNotFound(BUDGETS_MESSAGES['NOT_FOUND'])

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = BUDGETS_MESSAGES['DELETE_SUCCESS']
        return response
    
#===============================================================================

class BudgetMovementsListAPIView(generics.ListAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.get(pk=self.kwargs['pk']).movements.all()
    
#===============================================================================

class BudgetMovementsCreateAPIView(generics.CreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        try:
            serializer.save()
        except InvalidBudgetData:
            raise InvalidBudgetData(BUDGETS_MESSAGES['INVALID_DATA'])
        except BudgetAlreadyExists:
            raise BudgetAlreadyExists(BUDGETS_MESSAGES['ALREADY_EXISTS'])

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = BUDGETS_MESSAGES['CREATE_SUCCESS']

        return response
    
#===============================================================================

class BudgetMovementsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_object(self):
        try:
            return Budget.objects.get(pk=self.kwargs['pk'])
        except Budget.DoesNotExist:
            raise BudgetNotFound
        
#===============================================================================

class BudgetMovementsUpdateAPIView(generics.UpdateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_update(self, serializer):
        try:
            serializer.save()
        except InvalidBudgetData:
            raise InvalidBudgetData(BUDGETS_MESSAGES['INVALID_DATA'])
        except BudgetAlreadyExists:
            raise BudgetAlreadyExists(BUDGETS_MESSAGES['ALREADY_EXISTS'])
        except InvalidBudgetStatus:
            raise InvalidBudgetStatus(BUDGETS_MESSAGES['INVALID_STATUS'])

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = BUDGETS_MESSAGES['UPDATE_SUCCESS']
        return response
    
#===============================================================================

class BudgetMovementsDestroyAPIView(generics.DestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except BudgetNotFound:
            raise BudgetNotFound(BUDGETS_MESSAGES['NOT_FOUND'])

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = BUDGETS_MESSAGES['DELETE_SUCCESS']
        return
    
#===============================================================================

