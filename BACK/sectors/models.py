from django.db import models
from accounts.models import User

#=================================================================================================================

class Direction(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name='Nome')
    description = models.TextField(blank=True,null=True,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Atualizado em')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='directions_created',verbose_name='Criado por')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='directions_updated',verbose_name='Atualizado por')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Direção'
        verbose_name_plural = 'Direções'

#=================================================================================================================

class Management(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='gerencias',verbose_name='Direção')
    name = models.CharField(max_length=100,verbose_name='Nome')
    description = models.TextField(blank=True,null=True,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Atualizado em')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='management_created',verbose_name='Criado por')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='management_updated',verbose_name='Atualizado por')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gerência'
        verbose_name_plural = 'Gerências'
        unique_together = ('direction', 'name')
        ordering = ['name']

#=================================================================================================================

class Coordination(models.Model):
    management = models.ForeignKey(Management, on_delete=models.CASCADE, related_name='coordenacoes',verbose_name='Gerência')
    name = models.CharField(max_length=100,verbose_name='Nome')
    description = models.TextField(blank=True,null=True,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Atualizado em')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coordination_created',verbose_name='Criado por')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coordination_updated',verbose_name='Atualizado por')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Coordenação'
        verbose_name_plural = 'Coordenações'
        unique_together = ('management', 'name')
        ordering = ['name']