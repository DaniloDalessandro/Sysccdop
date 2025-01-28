from django.core.exceptions import ValidationError

def validate_name(value):
    if not value.isalpha():
        raise ValidationError('O nome deve conter apenas letras.')

def validate_description(value):
    if len(value) < 10:
        raise ValidationError('A descrição deve ter pelo menos 10 caracteres.')
