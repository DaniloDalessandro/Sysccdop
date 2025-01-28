from rest_framework.exceptions import APIException

class EmployeeNotFound(APIException):
    status_code = 404
    default_detail = 'Funcionário não encontrado.'
    default_code = 'employee_not_found'

class InvalidEmployeeData(APIException):
    status_code = 400
    default_detail = 'Os dados fornecidos para o funcionário são inválidos.'
    default_code = 'invalid_employee_data'

class EmployeeAlreadyExists(APIException):
    status_code = 400
    default_detail = 'O funcionário já existe.'
    default_code = 'employee_already_exists'

class EmployeeNotDeleted(APIException):
    status_code = 400
    default_detail = 'O funcionário não pode ser excluído.'
    default_code = 'employee_not_deleted'

    

