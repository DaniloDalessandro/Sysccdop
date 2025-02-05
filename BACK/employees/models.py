from django.db import models
from sectors.models import Direction, Management, Coordination
from accounts.models import User
from services.services_contract import generate_protocol_number

class Employee(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    employee_id = models.IntegerField(null=True, blank=True, verbose_name='Matrícula', unique=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True)
    management = models.ForeignKey(Management, on_delete=models.SET_NULL, null=True)
    coordination = models.ForeignKey(Coordination, on_delete=models.SET_NULL, null=True)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=50, null=True, blank=True)
    STATUS = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
    ]
    status = models.CharField(max_length=7, choices=STATUS, default='ATIVO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees_created', verbose_name='Criado por')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees_updated', verbose_name='Atualizado por')

    def save(self, *args, **kwargs):
        if not self.protocol_number:
            self.protocol_number = generate_protocol_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name or "Colaborador sem nome"
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'