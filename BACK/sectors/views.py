from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Direction,Management,Coordination
from .serializers import DirectionSerializer,ManagementSerializer,CoordinationSerializer
from .utils.exceptions import DirectionNotFound,ManagementNotFound,CoordinationNotFound
from .utils.messages import DIRECTION_MESSAGE, MANAGEMENT_MESSAGE, COORDINATION_MESSAGE


#============================================================================================================

class DirectionListAPIView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

#============================================================================================================

class DirectionCreateAPIView(generics.CreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = DIRECTION_MESSAGE['CREATE_SUCCESS']
        return response
    
#============================================================================================================

class DirectionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

    def get_object(self):
        try:
            return Direction.objects.get(pk=self.kwargs['pk'])
        except Direction.DoesNotExist:
            raise Direction
        
#============================================================================================================

class DirectionUpdateAPIView(generics.UpdateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = DIRECTION_MESSAGE['UPDATE_SUCCESS']
        return response
    
#============================================================================================================

class DirectionDestroyAPIView(generics.DestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = DIRECTION_MESSAGE['DELETE_SUCCESS']
        return response
    
#============================================================================================================

class ManagementListAPIView(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer

#============================================================================================================

class ManagementCreateAPIView(generics.CreateAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = MANAGEMENT_MESSAGE['CREATE_SUCCESS']
        return response
    
#============================================================================================================

class ManagementRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer

    def get_object(self):
        try:
            return Management.objects.get(pk=self.kwargs['pk'])
        except Management.DoesNotExist:
            raise ManagementNotFound
        
#============================================================================================================

class ManagementUpdateAPIView(generics.UpdateAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = MANAGEMENT_MESSAGE['UPDATE_SUCCESS']
        return response
    
#============================================================================================================

class ManagementDestroyAPIView(generics.DestroyAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = MANAGEMENT_MESSAGE['DELETE_SUCCESS']
        return response
    
#============================================================================================================

class CoordinationListAPIView(generics.ListAPIView):
    queryset = Coordination.objects.all()
    serializer_class = CoordinationSerializer

#============================================================================================================

class CoordinationCreateAPIView(generics.CreateAPIView):
    queryset = Coordination.objects.all()
    serializer_class = CoordinationSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = COORDINATION_MESSAGE['CREATE_SUCCESS']
        return response
    
#============================================================================================================

class CoordinationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Coordination.objects.all()
    serializer_class = CoordinationSerializer

    def get_object(self):
        try:
            return Coordination.objects.get(pk=self.kwargs['pk'])
        except Coordination.DoesNotExist:
            raise CoordinationNotFound
        
#============================================================================================================

class CoordinationUpdateAPIView(generics.UpdateAPIView):
    queryset = Coordination.objects.all()
    serializer_class = CoordinationSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = COORDINATION_MESSAGE['UPDATE_SUCCESS']
        return response
    
#============================================================================================================

class CoordinationDestroyAPIView(generics.DestroyAPIView):
    queryset = Coordination.objects.all()
    serializer_class = CoordinationSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = COORDINATION_MESSAGE['DELETE_SUCCESS']
        return response
    
#============================================================================================================
