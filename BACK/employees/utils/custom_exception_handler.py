from rest_framework.views import exception_handler
from .exceptions import EmployeeAlreadyExists, EmployeeNotFound, InvalidEmployeeData, EmployeeNotDeleted
from .messages import EMPLOYEES_MESSAGES

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Personaliza a resposta para exceções específicas
        if isinstance(exc, EmployeeAlreadyExists):
            response.data['message'] = EMPLOYEES_MESSAGES['ALREADY_EXISTS']
        elif isinstance(exc, EmployeeNotFound):
            response.data['message'] = EMPLOYEES_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidEmployeeData):
            response.data['message'] = EMPLOYEES_MESSAGES['INVALID_DATA']
        elif isinstance(exc, EmployeeNotDeleted):
            response.data['message'] = EMPLOYEES_MESSAGES['NOT_DELETED']                       
        
    return response