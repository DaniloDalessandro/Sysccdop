from django.db import models
from sectors.models import Direction, Management, Coordination

class Employee(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    employee_id = models.IntegerField(null=True, blank=True, verbose_name='Matrícula', unique=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True)
    management = models.ForeignKey(Management, on_delete=models.SET_NULL, null=True)
    coordination = models.ForeignKey(Coordination, on_delete=models.SET_NULL, null=True)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.full_name or "Colaborador sem nome"
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'