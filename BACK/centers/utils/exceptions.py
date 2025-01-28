from rest_framework.exceptions import APIException

class ManagementCenterNotFound(APIException):
    status_code = 404
    default_detail = 'Management Center não encontrado.'
    default_code = 'management_center_not_found'

class InvalidManagementCenterData(APIException):
    status_code = 400
    default_detail = 'Os dados fornecidos para o Management Center são inválidos.'
    default_code = 'invalid_management_center_data'
