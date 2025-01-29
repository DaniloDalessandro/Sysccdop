from django.db import models
from django.core.validators import MinValueValidator
from centers.models import Management_Center


#===============================================================================
class Budget(models.Model):
    BUDGET_CLASSES = [
        ('CAPEX', 'CAPEX'),
        ('OPEX', 'OPEX'),
    ]
    year = models.PositiveIntegerField()
    category = models.CharField(max_length=5, choices=BUDGET_CLASSES)
    management_center = models.ForeignKey(
        Management_Center, 
        on_delete=models.CASCADE, 
        related_name='budgets'
    )
    total_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)]
    )
    available_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)], 
        default=0.0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} {self.year} - {self.management_center.name}"
    
    class Meta:
        unique_together = ['year', 'category', 'management_center']
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'

#===============================================================================

class BudgetMovement(models.Model):
    source = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='outgoing_movements')
    destination = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='incoming_movements')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    movement_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.source} -> {self.destination} ({self.amount})"
    
    class Meta:
        verbose_name = 'Movimentação de Orçamento'
        verbose_name_plural = 'Movimentações de Orçamento'
        ordering = ['-movement_date']

