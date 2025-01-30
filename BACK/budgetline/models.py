from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import User
from budgets.models import Budget
from employees.models import Employee
from centers.models import Management_Center, Requesting_Center

class BudgetLine(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.PROTECT, related_name='budget_lines',verbose_name='Orçamento')
    BUDGET_CATEGORY_CHOICES = [
        ('CAPEX', 'CAPEX'),
        ('OPEX', 'OPEX'),
    ]
    category = models.CharField(
        max_length=100, 
        choices=BUDGET_CATEGORY_CHOICES, 
        blank=True, 
        null=True, 
        verbose_name='Categoria'
    )

    EXPENSE_TYPE_CHOICES = [
        ('Base Principal', 'Base Principal'),
        ('Serviços Especializados', 'Serviços Especializados'),
        ('Despesas Compartilhadas', 'Despesas Compartilhadas'),
    ]
    expense_type = models.CharField(
        max_length=100, 
        choices=EXPENSE_TYPE_CHOICES, 
        verbose_name='Expense Type'
    )

    managing_cost_center = models.ForeignKey(
        Management_Center, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='budget_lines'
    )
    requesting_cost_center = models.ForeignKey(
        Requesting_Center, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    summary_description = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        verbose_name='Descrição resumida'
    )
    object = models.CharField(
        max_length=80, 
        blank=True, 
        null=True, 
        verbose_name='Object'
    )

    BUDGET_CLASSIFICATION_CHOICES = [
        ('NOVO', 'NOVO'),
        ('RENOVAÇÃO', 'RENOVAÇÃO'),
        ('CARY OVER', 'CARY OVER'),
        ('REPLANEJAMENTO', 'REPLANEJAMENTO'),
        ('N/A', 'N/A'),
    ]
    budget_classification = models.CharField(
        max_length=100, 
        choices=BUDGET_CLASSIFICATION_CHOICES, 
        null=True, 
        blank=True
    )

    possible_fiscal = models.ForeignKey(
        Employee, 
        on_delete=models.PROTECT, 
        related_name='possible_contract_fiscal', 
        blank=True,
        null=True,
        verbose_name='Fiscal Principal'
    )

    CONTRACT_TYPE_CHOICES = [
        ('SERVIÇO', 'SERVIÇO'),
        ('FORNECIMENTO', 'FORNECIMENTO'),
        ('ASSINATURA', 'ASSINATURA'),
        ('FORNECIMENTO/SERVIÇO', 'FORNECIMENTO/SERVIÇO'),
    ]
    contract_type = models.CharField(
        max_length=100, 
        choices=CONTRACT_TYPE_CHOICES, 
        blank=True, 
        null=True,
        verbose_name='Tipo de Contrato'
    )

    PROCUREMENT_TYPE_CHOICES = [
        ('LICITAÇÃO', 'LICITAÇÃO'),
        ('DISPENSA EM RAZÃO DO VALOR', 'DISPENSA EM RAZÃO DO VALOR'),
        ('CONVÊNIO', 'CONVÊNIO'),
        ('FUNDO FIXO', 'FUNDO FIXO'),
        ('INEXIGIBILIDADE', 'INEXIGIBILIDADE'),
        ('ATA DE REGISTRO DE PREÇO', 'ATA DE REGISTRO DE PREÇO'),
        ('ACORDO DE COOPERAÇÃO', 'ACORDO DE COOPERAÇÃO'),
        ('APOSTILAMENTO', 'APOSTILAMENTO'),
    ]
    probable_procurement_type = models.CharField(
        max_length=100, 
        choices=PROCUREMENT_TYPE_CHOICES,
        verbose_name='Tipo de Aquisição'
    )
    
    budgeted_amount = models.FloatField(
        default=0, 
        validators=[MinValueValidator(0.01)],
        verbose_name='Valor Orçado'
    )

    PROCESS_STATUS_CHOICES = [
        ('VENCIDO', 'VENCIDO'),
        ('DENTRO DO PRAZO', 'DENTRO DO PRAZO'),
        ('ELABORADO COM ATRASO', 'ELABORADO COM ATRASO'),
        ('ELABORADO NO PRAZO', 'ELABORADO NO PRAZO'),
    ]
    process_status = models.CharField(
        max_length=100, 
        choices=PROCESS_STATUS_CHOICES, 
        blank=True, 
        null=True,
        verbose_name='Status do Processo'
    )

    CONTRACT_STATUS_CHOICES = [
        ('DENTRO DO PRAZO', 'DENTRO DO PRAZO'),
        ('CONTRATADO NO PRAZO', 'CONTRATADO NO PRAZO'),
        ('CONTRATADO COM ATRASO', 'CONTRATADO COM ATRASO'),
        ('PRAZO VENCIDO', 'PRAZO VENCIDO'),
        ('LINHA TOTALMENTE REMANEJADA', 'LINHA TOTALMENTE REMANEJADA'),
        ('LINHA TOTALMENTE EXECUTADA', 'LINHA TOTALMENTE EXECUTADA'),
        ('LINHA DE PAGAMENTO', 'LINHA DE PAGAMENTO'),
        ('LINHA PARCIALMENTE REMANEJADA', 'LINHA PARCIALMENTE REMANEJADA'),
        ('LINHA PARCIALMENTE EXECUTADA', 'LINHA PARCIALMENTE EXECUTADA'),
        ('N/A', 'N/A'),
    ]
    contract_status = models.CharField(
        max_length=100, 
        choices=CONTRACT_STATUS_CHOICES, 
        blank=True, 
        null=True,
        verbose_name='Status do Contrato'
    )

    contract_notes = models.TextField(
        max_length=400, 
        blank=True, 
        null=True,
        verbose_name='Observações'
    
    )
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Atualizado em')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='budget_lines_created',verbose_name='Criado por')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='budget_lines_updated',verbose_name='Atualizado por')   
   
    def __str__(self):
        return self.summary_description or "Linha orçamentaria desconhecida"

    class Meta:
        verbose_name = 'Linha Orçamentária'
        verbose_name_plural = 'Linhas Orçamentárias'
        
