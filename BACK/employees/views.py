from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from .utils.exceptions import EmployeeNotFound
from .utils.messages import EMPLOYEES_MESSAGES

#============================================================================================================

class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#============================================================================================================

class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = EMPLOYEES_MESSAGES['CREATE_SUCCESS']
        return response
    
#============================================================================================================

class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_object(self):
        try:
            return Employee.objects.get(pk=self.kwargs['pk'])
        except Employee.DoesNotExist:
            raise EmployeeNotFound
        
#============================================================================================================

class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = EMPLOYEES_MESSAGES['UPDATE_SUCCESS']
        return response
    
#============================================================================================================

class EmployeeDestroyAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = EMPLOYEES_MESSAGES['DELETE_SUCCESS']
        return response