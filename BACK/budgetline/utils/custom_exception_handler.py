from rest_framework.views import exception_handler
from .exceptions import BudgetLineNotFound, InvalidBudgetLineData, BudgetLineAlreadyExists, InvalidBudgetLineStatus
from .messages import BUDGETSLINE_MESSAGES

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Personaliza a resposta para exceções específicas
        if isinstance(exc, BudgetLineNotFound):
            response.data['message'] = BUDGETSLINE_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidBudgetLineData):
            response.data['message'] = BUDGETSLINE_MESSAGES['INVALID_DATA']
        elif isinstance(exc, BudgetLineAlreadyExists):
            response.data['message'] = BUDGETSLINE_MESSAGES['ALREADY_EXISTS']
        elif isinstance(exc, InvalidBudgetLineStatus):
            response.data['message'] = BUDGETSLINE_MESSAGES['INVALID_STATUS']           
        
    return response
