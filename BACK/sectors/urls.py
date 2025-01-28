from django.urls import path

from .views import (
    DirectionListAPIView,
    DirectionCreateAPIView,
    DirectionRetrieveAPIView,
    DirectionUpdateAPIView,
    DirectionDestroyAPIView,
    #=======================
    ManagementListAPIView,
    ManagementCreateAPIView,
    ManagementRetrieveAPIView,
    ManagementUpdateAPIView,
    ManagementDestroyAPIView,
    #=======================
    CoordinationListAPIView,  
    CoordinationCreateAPIView,
    CoordinationRetrieveAPIView,
    CoordinationUpdateAPIView,
    CoordinationDestroyAPIView,
)


urlpatterns = [
    path('direction/', DirectionListAPIView.as_view(), name='direction-list'),
    path('direction/create/', DirectionCreateAPIView.as_view(), name='direction-create'),
    path('direction/<int:pk>/', DirectionRetrieveAPIView.as_view(), name='direction-detail'),
    path('direction/<int:pk>/update/', DirectionUpdateAPIView.as_view(), name='direction-update'),
    path('direction/<int:pk>/delete/', DirectionDestroyAPIView.as_view(), name='direction-delete'),
    #=============================================================================================
    path('management/', ManagementListAPIView.as_view(), name='management-list'),
    path('management/create/', ManagementCreateAPIView.as_view(), name='management-create'),
    path('management/<int:pk>/', ManagementRetrieveAPIView.as_view(), name='management-detail'),
    path('management/<int:pk>/update/', ManagementUpdateAPIView.as_view(), name='management-update'),
    path('management/<int:pk>/delete/', ManagementDestroyAPIView.as_view(), name='management-delete'),
    #=============================================================================================
    path('coordinator/', CoordinationListAPIView.as_view(), name='coordinator-list'),
    path('coordinator/create/', CoordinationCreateAPIView.as_view(), name='coordinator-create'),
    path('coordinator/<int:pk>/', CoordinationRetrieveAPIView.as_view(), name='coordinator-detail'),
    path('coordinator/<int:pk>/update/', CoordinationUpdateAPIView.as_view(), name='coordinator-update'),
    path('coordinator/<int:pk>/delete/', CoordinationDestroyAPIView.as_view(), name='coordinator-delete'),
]