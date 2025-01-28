from rest_framework.exceptions import APIException

class DirectionNotFound(APIException):
    status_code = 404
    default_detail = 'Direcão não encontrado.'
    default_code = 'direction_not_found'

class InvalidDirectionData(APIException):
    status_code = 400
    default_detail = 'Os dados fornecidos para a Direcão são inválidos.'
    default_code = 'invalid_direction_data'

class DirectionAlreadyExists(APIException):
    status_code = 400
    default_detail = 'A direção já existe.'
    default_code = 'direction_already_exists'

class ManagementNotFound(APIException):
    status_code = 404
    default_detail = 'Gerência não encontrada.'
    default_code = 'management_center_not_found'

class InvalidManagementData(APIException):
    status_code = 400
    default_detail = 'Os dados fornecidos para o Management Center são inválidos.'
    default_code = 'invalid_management_center_data'

class ManagementAlreadyExists(APIException):
    status_code = 400
    default_detail = 'O centro de gestão já existe.'
    default_code = 'management_center_already_exists'

class CoordinationNotFound(APIException):
    status_code = 404
    default_detail = 'Coordenação não encontrado.'
    default_code = 'coordination_not_found'

class InvalidCoordinationData(APIException):
    status_code = 400
    default_detail = 'Os dados fornecidos para a coordenação são inválidos.'
    default_code = 'invalid_coordination_data'

class CoordinationAlreadyExists(APIException):
    status_code = 400
    default_detail = 'A coordenação já existe.'
    default_code = 'coordination_already_exists'
