from django.db import models
from .utils.validators import validate_name

class Management_Center(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[validate_name])
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Centro Gestor'
        verbose_name_plural = 'Centros Gestores'
        ordering = ['name']
    
#=================================================================================================================

class Requesting_Center(models.Model):
    management_center = models.ForeignKey(Management_Center, on_delete=models.CASCADE, related_name='solicitantes')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Centro Solicitante'
        verbose_name_plural = 'Centros Solicitantes'
        unique_together = ('management_center', 'name')
        ordering = ['name']