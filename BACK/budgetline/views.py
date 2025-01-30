from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import BudgetLine
from .serializers import BudgetLineSerializer
from .utils.exceptions import BudgetLineNotFound, InvalidBudgetLineData, BudgetLineAlreadyExists, InvalidBudgetLineStatus, InvalidBudgetLineMovement, BudgetLineMovementNotFound
from .utils.messages import BUDGETSLINE_MESSAGES

#=======================================================================================================

class BudgetLineListAPIView(generics.ListAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer

#=======================================================================================================

class BudgetLineCreateAPIView(generics.CreateAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(created_by=user, updated_by=user) 
        else:
            serializer.save()  

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = "Linha orçamentaria criada com sucesso!"
        return response
    
#=======================================================================================================

class BudgetLineRetrieveAPIView(generics.RetrieveAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer

    def get_object(self):
        try:
            return BudgetLine.objects.get(pk=self.kwargs['pk'])
        except BudgetLine.DoesNotExist:
            raise BudgetLineNotFound
        
#=======================================================================================================

class BudgetLineUpdateAPIView(generics.UpdateAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = BUDGETSLINE_MESSAGES['UPDATE_SUCCESS']
        return response
    
#=======================================================================================================

class BudgetLineDestroyAPIView(generics.DestroyAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': BUDGETSLINE_MESSAGES['DELETE_SUCCESS']}, status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()

#=======================================================================================================

class BudgetLineMovementCreateAPIView(generics.CreateAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(created_by=user, updated_by=user) 
        else:
            serializer.save()  

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = BUDGETSLINE_MESSAGES['CREATE_SUCCESS']
        return response
    
#=======================================================================================================

class BudgetLineMovementRetrieveAPIView(generics.RetrieveAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer

    def get_object(self):
        try:
            return BudgetLine.objects.get(pk=self.kwargs['pk'])
        except BudgetLine.DoesNotExist:
            raise BudgetLineMovementNotFound
        
#=======================================================================================================

class BudgetLineMovementUpdateAPIView(generics.UpdateAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = BUDGETSLINE_MESSAGES['UPDATE_SUCCESS']
        return response
    
#=======================================================================================================

class BudgetLineMovementDestroyAPIView(generics.DestroyAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': BUDGETSLINE_MESSAGES['DELETE_SUCCESS']}, status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()

#=======================================================================================================

class BudgetLineMovementListAPIView(generics.ListAPIView):
    queryset = BudgetLine.objects.all()
    serializer_class = BudgetLineSerializer
