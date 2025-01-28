from django.core.exceptions import ValidationError

def validate_employee_name(value):
    if not value.isalpha():
        raise ValidationError('O nome do funcionário deve conter apenas letras.')
    if len(value) < 2:
        raise ValidationError('O nome do funcionário deve conter pelo menos 2 caracteres.')


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('O CPF deve conter apenas números.')
    if len(value) != 11:
        raise ValidationError('O CPF deve conter 11 dígitos.')
    if len(set(value)) == 1:
        raise ValidationError('O CPF não pode conter todos os dígitos iguais.')
    # Validação dos dígitos verificadores
    def calculate_digit(digits):
        sum = 0
        for i, digit in enumerate(digits):
            sum += int(digit) * (len(digits) + 1 - i)
        remainder = sum % 11
        return '0' if remainder < 2 else str(11 - remainder)

    first_nine_digits = value[:9]
    first_check_digit = calculate_digit(first_nine_digits)
    second_check_digit = calculate_digit(first_nine_digits + first_check_digit)

    if value[-2:] != first_check_digit + second_check_digit:
        raise ValidationError('O CPF é inválido.')
    