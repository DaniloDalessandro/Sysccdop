from django.urls import path
from .views import (
    ManagementCenterListAPIView,
    ManagementCenterCreateAPIView,
    ManagementCenterRetrieveAPIView,
    ManagementCenterUpdateAPIView,
    ManagementCenterDestroyAPIView,
    #==============================
    RequestingCenterCreateAPIView,
    RequestingCenterListAPIView,
    RequestingCenterUpdateAPIView,
    RequestingCenterRetrieveAPIView,
    RequestingCenterDestroyAPIView,
)

urlpatterns = [
    path('management-center/', ManagementCenterListAPIView.as_view(), name='management-center-list'),
    path('management-center/create/', ManagementCenterCreateAPIView.as_view(), name='management-center-create'),
    path('management-center/<int:pk>/', ManagementCenterRetrieveAPIView.as_view(), name='management-center-retrieve'),
    path('management-center/update/<int:pk>/', ManagementCenterUpdateAPIView.as_view(), name='management-center-update'),
    path('management-center/delete/<int:pk>/', ManagementCenterDestroyAPIView.as_view(), name='management-center-destroy'),
    #============================================================================================================
    path('requesting-center/', RequestingCenterListAPIView.as_view(), name='requesting-center-list'),
    path('requesting-center/create/', RequestingCenterCreateAPIView.as_view(), name='requesting-center-create'),
    path('requesting-center/<int:pk>/', RequestingCenterRetrieveAPIView.as_view(), name='requesting-center-retrieve'),
    path('requesting-center/update/<int:pk>/', RequestingCenterUpdateAPIView.as_view(), name='requesting-center-update'),
    path('requesting-center/delete/<int:pk>/', RequestingCenterDestroyAPIView.as_view(), name='requesting-center-destroy'),
]
