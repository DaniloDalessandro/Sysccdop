from django.urls import path
from .views import EmployeeUpdateAPIView, EmployeeDestroyAPIView,EmployeeCreateAPIView,EmployeeListAPIView,EmployeeRetrieveAPIView

urlpatterns = [
    path('', EmployeeListAPIView.as_view(), name='employee-list'),
    path('create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='employee-retrieve'),
    path('<int:pk>/update/', EmployeeUpdateAPIView.as_view(), name='employee-update'),
    path('<int:pk>/destroy/', EmployeeDestroyAPIView.as_view(), name='employee-destroy'),
]

