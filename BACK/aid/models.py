from django.db import models
from budgetline.models import BudgetLine
from employees.models import Employee
from django.core.validators import MinValueValidator

class Assistance(models.Model):
    ASSISTANCE_TYPES = [
    ('UNICO', 'Pagamento Único'),
    ('PARCELADO', 'Parcelado'),
    ]

    STATUS_CHOICES = [
    ('AGUARDANDO', 'Aguardando Início'),
    ('ATIVO', 'Ativo'),
    ('CONCLUIDO', 'Concluído'),
    ('CANCELADO', 'Cancelado'),
    ]

    TYPE_CHOICES = [
    ('GRADUACAO', 'Graduação'),
    ('POS_GRADUACAO', 'Pós-Graduação'),
    ('AUXILIO_CHECHE_ESCOLA', 'Auxílio Creche Escola'),
    ('LINGUA_ESTRANGEIRA', 'Língua Estrangeira'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assistances',verbose_name='Funcionário')
    budget_line = models.ForeignKey(BudgetLine, on_delete=models.CASCADE, related_name='assistances',verbose_name='Linha Orçamentária')
    assistance_type = models.CharField(max_length=10, choices=ASSISTANCE_TYPES,verbose_name='Tipo de Assistência')
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True, blank=True,verbose_name='Tipo')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)],verbose_name='Valor Total')
    installment_count = models.PositiveIntegerField(null=True, blank=True,verbose_name='Número de Parcelas')
    amount_per_installment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,verbose_name='Valor por Parcela')
    start_date = models.DateField(verbose_name='Data de Início')
    end_date = models.DateField(null=True, blank=True,verbose_name='Data de Término')
    notes = models.TextField(blank=True,verbose_name='Observações')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='AGUARDANDO',verbose_name='Status')

    def __str__(self):
        return self.employee.name + ' - ' + self.budget_line.name

    class Meta:
        ordering = ['start_date']
        verbose_name = 'Assistência'
        verbose_name_plural = 'Assistências'

# =================================================================================================================

class AssistanceInstallment(models.Model):
    PAYMENT_STATUS = [
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
    ]

    assistance = models.ForeignKey(Assistance, on_delete=models.CASCADE, related_name='installments',verbose_name='Assistência')
    number = models.PositiveIntegerField(verbose_name='Número')
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Valor')
    due_date = models.DateField(verbose_name='Data de Vencimento')
    paid = models.BooleanField(default=False,verbose_name='Pago')
    payment_date = models.DateField(null=True, blank=True,verbose_name='Data de Pagamento')

    class Meta:
        ordering = ['due_date']
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'
