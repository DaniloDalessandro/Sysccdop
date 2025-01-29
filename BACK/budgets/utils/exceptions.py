from rest_framework.exceptions import APIException

class BudgetNotFound(APIException):
    status_code = 404
    default_detail = 'Orçamento não encontrado.'
    default_code = 'budget_not_found'

class InvalidBudgetData(APIException):
    status_code = 400
    default_detail = 'Os dados fornecidos para o Orçamento são inválidos.'
    default_code = 'invalid_budget_data'

class BudgetAlreadyExists(APIException):
    status_code = 400
    default_detail = 'O orçamento já existe.'
    default_code = 'budget_already_exists'

class InvalidBudgetStatus(APIException):
    status_code = 400
    default_detail = 'O status do orçamento é inválido.'
    default_code = 'invalid_budget_status'

class InvalidBudgetMovement(APIException):
    status_code = 400
    default_detail = 'A movimentação de orçamento é inválida.'
    default_code = 'invalid_budget_movement'

class BudgetMovementNotFound(APIException):
    status_code = 404
    default_detail = 'Movimentação de orçamento não encontrada.'
    default_code = 'budget_movement_not_found'

class BudgetMovementAlreadyExists(APIException):
    status_code = 400
    default_detail = 'A movimentação de orçamento já existe.'
    default_code = 'budget_movement_already_exists'

class InvalidBudgetMovementAmount(APIException):
    status_code = 400
    default_detail = 'O valor da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_amount'

class InvalidBudgetMovementDate(APIException):
    status_code = 400
    default_detail = 'A data da movimentação de orçamento é inválida.'
    default_code = 'invalid_budget_movement_date'

class InvalidBudgetMovementNotes(APIException):
    status_code = 400
    default_detail = 'As notas da movimentação de orçamento são inválidas.'
    default_code = 'invalid_budget_movement_notes'

class InvalidBudgetMovementSource(APIException):
    status_code = 400
    default_detail = 'A origem da movimentação de orçamento é inválida.'
    default_code = 'invalid_budget_movement_source'

class InvalidBudgetMovementDestination(APIException):
    status_code = 400
    default_detail = 'O destino da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_destination'

class InvalidBudgetMovementSourceDestination(APIException):
    status_code = 400
    default_detail = 'A origem e o destino da movimentação de orçamento são inválidos.'
    default_code = 'invalid_budget_movement_source_destination'

class InvalidBudgetMovementSourceAmount(APIException):
    status_code = 400
    default_detail = 'O valor da origem da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_source_amount'

class InvalidBudgetMovementDestinationAmount(APIException):
    status_code = 400
    default_detail = 'O valor do destino da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_destination_amount'

class InvalidBudgetMovementSourceAvailableAmount(APIException):
    status_code = 400
    default_detail = 'O valor disponível na origem da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_source_available_amount'

class InvalidBudgetMovementDestinationAvailableAmount(APIException):
    status_code = 400
    default_detail = 'O valor disponível no destino da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_destination_available_amount'

class InvalidBudgetMovementSourceCategory(APIException):
    status_code = 400
    default_detail = 'A categoria da origem da movimentação de orçamento é inválida.'
    default_code = 'invalid_budget_movement_source_category'

class InvalidBudgetMovementDestinationCategory(APIException):
    status_code = 400
    default_detail = 'A categoria do destino da movimentação de orçamento é inválida.'
    default_code = 'invalid_budget_movement_destination_category'

class InvalidBudgetMovementSourceManagementCenter(APIException):
    status_code = 400
    default_detail = 'O centro de gestão da origem da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_source_management_center'

class InvalidBudgetMovementDestinationManagementCenter(APIException):  
    status_code = 400
    default_detail = 'O centro de gestão do destino da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_destination_management_center'

class InvalidBudgetMovementSourceYear(APIException):
    status_code = 400
    default_detail = 'O ano da origem da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_source_year'

class InvalidBudgetMovementDestinationYear(APIException):
    status_code = 400
    default_detail = 'O ano do destino da movimentação de orçamento é inválido.'
    default_code = 'invalid_budget_movement_destination_year'




