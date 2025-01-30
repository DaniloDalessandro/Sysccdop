from django.urls import path

from .views import (
    BudgetLineListAPIView,
    BudgetLineCreateAPIView,
    BudgetLineRetrieveAPIView,
    BudgetLineUpdateAPIView,
    BudgetLineDestroyAPIView,
    #==============================
    BudgetLineMovementListAPIView,
    BudgetLineMovementCreateAPIView,
    BudgetLineMovementRetrieveAPIView,
    BudgetLineMovementUpdateAPIView,
    BudgetLineMovementDestroyAPIView,
)

urlpatterns = [
    path('budgetslines/', BudgetLineListAPIView.as_view(), name='budgetline-list'),
    path('budgetslines/create/', BudgetLineCreateAPIView.as_view(), name='budgetline-create'),
    path('budgetslines/<int:pk>/', BudgetLineRetrieveAPIView.as_view(), name='budgetline-retrieve'),
    path('budgetslines/<int:pk>/update/', BudgetLineUpdateAPIView.as_view(), name='budgetline-update'),
    path('budgetslines/<int:pk>/delete/', BudgetLineDestroyAPIView.as_view(), name='budgetline-destroy'),
    #==============================
    path('budgetlinemovements/', BudgetLineMovementListAPIView.as_view(), name='budgetlinemovement-list'),
    path('budgetlinemovements/create/', BudgetLineMovementCreateAPIView.as_view(), name='budgetlinemovement-create'),
    path('budgetlinemovements/<int:pk>/', BudgetLineMovementRetrieveAPIView.as_view(), name='budgetlinemovement-retrieve'),
    path('budgetlinemovements/<int:pk>/update/', BudgetLineMovementUpdateAPIView.as_view(), name='budgetlinemovement-update'),
    path('budgetlinemovements/<int:pk>/delete/', BudgetLineMovementDestroyAPIView.as_view(), name='budgetlinemovement-destroy'),
]