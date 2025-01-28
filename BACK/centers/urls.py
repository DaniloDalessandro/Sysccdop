from django.urls import path
from .views import (
    ManagementCenterListAPIView,
    ManagementCenterCreateAPIView,
    ManagementCenterRetrieveAPIView,
    ManagementCenterUpdateAPIView,
    ManagementCenterDestroyAPIView,
)

urlpatterns = [
    path('management-center/', ManagementCenterListAPIView.as_view(), name='management-center-list'),
    path('management-center/create/', ManagementCenterCreateAPIView.as_view(), name='management-center-create'),
    path('management-center/<int:pk>/', ManagementCenterRetrieveAPIView.as_view(), name='management-center-retrieve'),
    path('management-center/update/<int:pk>/', ManagementCenterUpdateAPIView.as_view(), name='management-center-update'),
    path('management-center/delete/<int:pk>/', ManagementCenterDestroyAPIView.as_view(), name='management-center-destroy'),
]
