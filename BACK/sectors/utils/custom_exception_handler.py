from rest_framework.views import exception_handler
from .exceptions import (DirectionNotFound,
                         InvalidDirectionData, 
                         DirectionAlreadyExists,
                         ManagementAlreadyExists,
                         ManagementNotFound,
                         InvalidManagementData, 
                         CoordinationNotFound, 
                         InvalidCoordinationData, 
                         CoordinationAlreadyExists
             ) 

from .messages import DIRECTION_MESSAGES, MANAGEMENT_MESSAGES, COORDINATION_MESSAGES

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Personaliza a resposta para exceções específicas
        if isinstance(exc, DirectionNotFound):
            response.data['message'] = DIRECTION_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidDirectionData):
            response.data['message'] = DIRECTION_MESSAGES['INVALID_DATA']
        elif isinstance(exc, DirectionAlreadyExists):
            response.data['message'] = DIRECTION_MESSAGES['ALREADY_EXISTS']
        elif isinstance(exc, ManagementNotFound):
            response.data['message'] = MANAGEMENT_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidManagementData):
            response.data['message'] = MANAGEMENT_MESSAGES['INVALID_DATA']
        elif isinstance(exc, ManagementAlreadyExists):
            response.data['message'] = MANAGEMENT_MESSAGES['ALREADY_EXISTS']
        elif isinstance(exc, CoordinationNotFound):
            response.data['message'] = COORDINATION_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidCoordinationData):
            response.data['message'] = COORDINATION_MESSAGES['INVALID_DATA']
        elif isinstance(exc, CoordinationAlreadyExists):
            response.data['message'] = COORDINATION_MESSAGES['ALREADY_EXISTS']  

    return response