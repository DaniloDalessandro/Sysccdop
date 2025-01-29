from django.urls import path

from .views import (BudgetsListAPIView,
                    BudgetCreateAPIView, 
                    BudgetRetrieveAPIView, 
                    BudgetUpdateAPIView, 
                    BudgetDestroyAPIView,
                    BudgetMovementsListAPIView,
                    BudgetMovementsCreateAPIView,
                    BudgetMovementsRetrieveAPIView,
                    BudgetMovementsUpdateAPIView,
                    BudgetMovementsDestroyAPIView
                    )


urlpatterns = [
    path('', BudgetsListAPIView.as_view(), name='budget_list'),
    path('create/', BudgetCreateAPIView.as_view(), name='budget_create'),
    path('retrieve/<int:pk>/', BudgetRetrieveAPIView.as_view(), name='budget_retrieve'),
    path('update/<int:pk>/', BudgetUpdateAPIView.as_view(), name='budget_update'),
    path('destroy/<int:pk>/', BudgetDestroyAPIView.as_view(), name='budget_destroy'),
    #===============================================================================
    path('movements/', BudgetMovementsListAPIView.as_view(), name='budget_movement_list'),
    path('movements/create/', BudgetMovementsCreateAPIView.as_view(), name='budget_movement_create'),
    path('movements/retrieve/<int:pk>/', BudgetMovementsRetrieveAPIView.as_view(), name='budget_movement_retrieve'),
    path('movements/update/<int:pk>/', BudgetMovementsUpdateAPIView.as_view(), name='budget_movement_update'),
    path('movements/destroy/<int:pk>/', BudgetMovementsDestroyAPIView.as_view(), name='budget_movement_destroy'),

]