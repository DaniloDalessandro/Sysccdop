from rest_framework.views import exception_handler
from .exceptions import BudgetNotFound, InvalidBudgetData,BudgetAlreadyExists,InvalidBudgetStatus
from .messages import BUDGETS_MESSAGES

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Personaliza a resposta para exceções específicas
        if isinstance(exc, BudgetNotFound):
            response.data['message'] = BUDGETS_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidBudgetData):
            response.data['message'] = BUDGETS_MESSAGES['INVALID_DATA']
        elif isinstance(exc, BudgetAlreadyExists):
            response.data['message'] = BUDGETS_MESSAGES['ALREADY_EXISTS']
        elif isinstance(exc, InvalidBudgetStatus):
            response.data['message'] = BUDGETS_MESSAGES['INVALID_STATUS']           
        
    return response
