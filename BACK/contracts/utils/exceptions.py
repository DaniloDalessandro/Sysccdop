from rest_framework.exceptions import APIException

class ContractNotFound(APIException):
    status_code = 404
    default_detail = 'Contrato não encontrado.'
    default_code = 'contract_not_found'

class InvalidContractData(APIException):
    status_code = 400
    default_detail = 'Os dados fornecidos para o contrato são inválidos.'
    default_code = 'invalid_contract_data'

class ContractAlreadyExists(APIException):
    status_code = 400
    default_detail = 'O contrato já existe.'
    default_code = 'contract_already_exists'

class ContractNotDeleted(APIException):
    status_code = 400
    default_detail = 'O contrato não pode ser excluído.'
    default_code = 'contract_not_deleted'