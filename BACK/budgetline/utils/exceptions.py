from rest_framework.exceptions import APIException

class BudgetLineNotFound(APIException):
    status_code = 404
    default_detail = 'Orçamento não encontrado.'
    default_code = 'budget_not_found'

class InvalidBudgetLineData(APIException):
    status_code = 400
    default_detail = 'Os dados fornecidos para o Orçamento são inválidos.'
    default_code = 'invalid_budget_data'

class BudgetLineAlreadyExists(APIException):
    status_code = 400
    default_detail = 'O orçamento já existe.'
    default_code = 'budget_already_exists'

class InvalidBudgetLineStatus(APIException):
    status_code = 400
    default_detail = 'O status do orçamento é inválido.'
    default_code = 'invalid_budget_status'

class InvalidBudgetLineMovement(APIException):
    status_code = 400
    default_detail = 'A movimentação de orçamento é inválida.'
    default_code = 'invalid_budget_movement'

class BudgetLineMovementNotFound(APIException):
    status_code = 404
    default_detail = 'Movimentação de orçamento não encontrada.'
    default_code = 'budget_movement_not_found'

    