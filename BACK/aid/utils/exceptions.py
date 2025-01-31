from rest_framework.exceptions import APIException

class AidNotFound(APIException):
    status_code = 404
    default_detail = 'Aid not found'
    default_code = 'aid_not_found'

class AidAlreadyExists(APIException):
    status_code = 400
    default_detail = 'Aid already exists'
    default_code = 'aid_already_exists'

class InvalidData(APIException):
    status_code = 400
    default_detail = 'Invalid data'
    default_code = 'invalid_data'

class NoData(APIException):
    status_code = 400
    default_detail = 'No data'
    default_code = 'no_data'

class InvalidToken(APIException):
    status_code = 400
    default_detail = 'Invalid token'
    default_code = 'invalid_token'

class InvalidCredentials(APIException):
    status_code = 400
    default_detail = 'Invalid credentials'
    default_code = 'invalid_credentials'