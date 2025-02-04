from django.db import IntegrityError
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Management_Center,Requesting_Center
from .serializers import ManagementCenterSerializer,RequestingCenterSerializer
from .utils.exceptions import ManagementCenterNotFound
from .utils.messages import MANAGEMENT_CENTER_MESSAGES

#=====================================================================================

class ManagementCenterListAPIView(generics.ListAPIView):
    queryset = Management_Center.objects.all()
    serializer_class = ManagementCenterSerializer

#=====================================================================================

class ManagementCenterCreateAPIView(generics.CreateAPIView):
    queryset = Management_Center.objects.all()
    serializer_class = ManagementCenterSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(created_by=user, updated_by=user) 
        else:
            serializer.save()  

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            response.data['message'] = MANAGEMENT_CENTER_MESSAGES['CREATE_SUCCESS']
        except IntegrityError:
            response = Response(
                {'message': MANAGEMENT_CENTER_MESSAGES['ALREADY_EXISTS']},
                status=status.HTTP_400_BAD_REQUEST
            )
        return response

#=====================================================================================

class ManagementCenterRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Management_Center.objects.all()
    serializer_class = ManagementCenterSerializer

    def get_object(self):
        try:
            return Management_Center.objects.get(pk=self.kwargs['pk'])
        except Management_Center.DoesNotExist:
            raise ManagementCenterNotFound

#=====================================================================================

class ManagementCenterUpdateAPIView(generics.UpdateAPIView):
    queryset = Management_Center.objects.all()
    serializer_class = ManagementCenterSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = MANAGEMENT_CENTER_MESSAGES['UPDATE_SUCCESS']
        return response

#=====================================================================================

class ManagementCenterDestroyAPIView(generics.DestroyAPIView):
    queryset = Management_Center.objects.all()
    serializer_class = ManagementCenterSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = MANAGEMENT_CENTER_MESSAGES['DELETE_SUCCESS']
        return response

#=====================================================================================

class RequestingCenterListAPIView(generics.ListAPIView):
    queryset = Requesting_Center.objects.all()
    serializer_class = RequestingCenterSerializer

#=====================================================================================

class RequestingCenterCreateAPIView(generics.CreateAPIView):
    queryset = Requesting_Center.objects.all()
    serializer_class = RequestingCenterSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(created_by=user, updated_by=user) 
        else:
            serializer.save()  

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = MANAGEMENT_CENTER_MESSAGES['CREATE_SUCCESS']
        return response

#=====================================================================================

class RequestingCenterRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Requesting_Center.objects.all()
    serializer_class = RequestingCenterSerializer

    def get_object(self):
        try:
            return Requesting_Center.objects.get(pk=self.kwargs['pk'])
        except Requesting_Center.DoesNotExist:
            raise ManagementCenterNotFound

#=====================================================================================

class RequestingCenterUpdateAPIView(generics.UpdateAPIView):
    queryset = Requesting_Center.objects.all()
    serializer_class = RequestingCenterSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = MANAGEMENT_CENTER_MESSAGES['UPDATE_SUCCESS']
        return response

#=====================================================================================

class RequestingCenterDestroyAPIView(generics.DestroyAPIView):
    queryset = Requesting_Center.objects.all()
    serializer_class = RequestingCenterSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = MANAGEMENT_CENTER_MESSAGES['DELETE_SUCCESS']
        return response

