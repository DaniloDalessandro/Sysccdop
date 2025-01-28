from rest_framework.views import exception_handler
from sectors.exceptions import ManagementCenterNotFound, InvalidManagementCenterData
from sectors.messages import MANAGEMENT_CENTER_MESSAGES

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Personaliza a resposta para exceções específicas
        if isinstance(exc, ManagementCenterNotFound):
            response.data['message'] = MANAGEMENT_CENTER_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidManagementCenterData):
            response.data['message'] = MANAGEMENT_CENTER_MESSAGES['INVALID_DATA']

    return response