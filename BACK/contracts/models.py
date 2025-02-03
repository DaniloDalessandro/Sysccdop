from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import User
from employees.models import Employee
from budgetline.models import BudgetLine

class Contract(models.Model):
    budget_line = models.ForeignKey(BudgetLine, on_delete=models.PROTECT, related_name='contracts')
    protocol_number = models.CharField(max_length=7, unique=True, blank=True, editable=False, verbose_name='Contrato')
    signing_date = models.DateField(null=True, blank=True,verbose_name='Data de Assinatura')
    expiration_date = models.DateField(null=True, blank=True,verbose_name='Data de Expiração')
    main_inspector = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='contracts_main_inspector', verbose_name='Fiscal Principal')
    substitute_inspector = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='contracts_substitute_inspector', verbose_name='Fiscal Substituto')
    PAYMENT_TYPE_CHOICES = [
        ('PAGAMENTO ÚNICO','PAGAMENTO ÚNICO'),
        ('PAGAMENTO ANUAL','PAGAMENTO ANUAL'),
        ('PAGAMENTO SEMANAL','PAGAMENTO SEMANAL'),
        ('PAGAMENTO MENSAL','PAGAMENTO MENSAL'),
        ('PAGAMENTO QUIZENAL','PAGAMENTO QUINZENAL'),
        ('PAGAMENTO TRIMESTRAL','PAGAMENTO TRIMESTRAL'),
        ('PAGAMENTO SEMESTRAL','PAGAMENTO SEMESTRAL'),
        ('PAGAMENTO SOB DEMANDA','PAGAMENTO SOB DEMANDA'),
    ]
    payment_nature = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=30,verbose_name='Natureza do Pagamento')
    description = models.CharField(max_length=255,verbose_name='Descrição')
    original_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)],verbose_name='Valor Original')
    current_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], default=0.0,verbose_name='Valor Atual')
    start_date = models.DateField(verbose_name='Data de Início')
    end_date = models.DateField(null=True, blank=True,verbose_name='Data de Término')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='contracts_created', verbose_name='Criado por')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='contracts_updated', verbose_name='Atualizado por')

    def __str__(self):
        return self.protocol_number
    
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['protocol_number']

#=======================================================================================================================

class ContractInstallment(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='installments')
    number = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    due_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('PENDENTE', 'Pendente'), ('PAGO', 'Pago'), ('ATRASADO', 'Atrasado')],
        default='PENDENTE',
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='aditivos_created')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='aditivos_updated')
    
    def __str__(self):
        return f"Installment {self.number} - {self.contract.description}"
    
    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'
        ordering = ['contract', 'number']

#=======================================================================================================================

class ContractAmendment(models.Model):
    AMENDMENT_TYPES = [
        ('ACRESCIMO_VALOR', 'Acréscimo de Valor'),
        ('REDUCAO_VALOR', 'Redução de Valor'),
        ('PRORROGACAO_PRAZO', 'Prorrogação de Prazo'),
    ]
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='Contrato')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    type = models.CharField(max_length=20, choices=AMENDMENT_TYPES,verbose_name='Tipo')
    value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)],verbose_name='Valor')
    additional_term = models.DateTimeField(null=True, blank=True,verbose_name='Prazo Adicional')  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='amendments_created',verbose_name='Criado por')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='amendments_updated',verbose_name='Atualizado por')
    
    def __str__(self):
        return f"{self.description} - {self.contract.description}"
    
    class Meta:
        verbose_name = 'Aditivo'
        verbose_name_plural = 'Aditivos'
        ordering = ['contract', 'created_at']
