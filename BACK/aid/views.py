from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Aid
from .serializers import AidSerializer
from .utils.exceptions import AidNotFound, AidAlreadyExists
from .utils.messages import AID_MESSAGES

#=======================================================================================================================

class AidListAPIView(generics.ListAPIView):
    queryset = Aid.objects.all()
    serializer_class = AidSerializer

#=======================================================================================================================

class AidCreateAPIView(generics.CreateAPIView):
    queryset = Aid.objects.all()
    serializer_class = AidSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = "Aid created successfully!"
        return response

#=======================================================================================================================

class AidRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Aid.objects.all()
    serializer_class = AidSerializer

    def get_object(self):
        try:
            return Aid.objects.get(pk=self.kwargs['pk'])
        except Aid.DoesNotExist:
            raise AidNotFound

#=======================================================================================================================

class AidUpdateAPIView(generics.UpdateAPIView):
    queryset = Aid.objects.all()
    serializer_class = AidSerializer

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data['message'] = AID_MESSAGES['UPDATE_SUCCESS']
        return response

#=======================================================================================================================

class AidDestroyAPIView(generics.DestroyAPIView):
    queryset = Aid.objects.all()
    serializer_class = AidSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        response.data['message'] = AID_MESSAGES['DELETE_SUCCESS']
        return response

