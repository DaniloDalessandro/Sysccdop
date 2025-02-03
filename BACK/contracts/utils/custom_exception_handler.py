from rest_framework.views import exception_handler
from .exceptions import ContractAlreadyExists, ContractNotFound, InvalidContractData, ContractNotDeleted
from .messages import CONTRACTS_MESSAGES

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Personaliza a resposta para exceções específicas
        if isinstance(exc, ContractAlreadyExists):
            response.data['message'] = CONTRACTS_MESSAGES['ALREADY_EXISTS']
        elif isinstance(exc, ContractNotFound):
            response.data['message'] = CONTRACTS_MESSAGES['NOT_FOUND']
        elif isinstance(exc, InvalidContractData):
            response.data['message'] = CONTRACTS_MESSAGES['INVALID_DATA']
        elif isinstance(exc, ContractNotDeleted):
            response.data['message'] = CONTRACTS_MESSAGES['NOT_DELETED']                       
        
    return response