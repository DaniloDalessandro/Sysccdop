from rest_framework.views import exception_handler
from aid.utils.messages import AID_MESSAGES
from .exceptions import AidNotFound, InvalidData, AidAlreadyExists, NoData, InvalidToken, InvalidCredentials

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Personaliza a resposta para exceções específicas
        if isinstance(exc, AidNotFound):
            response.data['message'] = AID_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidData):
            response.data['message'] = AID_MESSAGES['INVALID_DATA']
        elif isinstance(exc, AidAlreadyExists):
            response.data['message'] = AID_MESSAGES['ALREADY_EXISTS']
        elif isinstance(exc, NoData):
            response.data['message'] = AID_MESSAGES['NO_DATA']
        elif isinstance(exc, InvalidToken):
            response.data['message'] = AID_MESSAGES['INVALID_TOKEN']
        elif isinstance(exc, InvalidCredentials):
            response.data['message'] = AID_MESSAGES['INVALID_CREDENTIALS']

    return response