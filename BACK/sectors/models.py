from django.db import models

class Direction(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Direção'
        verbose_name_plural = 'Direções'

#=================================================================================================================

class Management(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='gerencias')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gerência'
        verbose_name_plural = 'Gerências'
        unique_together = ('direction', 'name')
        ordering = ['name']

#=================================================================================================================

class Coordination(models.Model):
    management = models.ForeignKey(Management, on_delete=models.CASCADE, related_name='coordenacoes')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Coordenação'
        verbose_name_plural = 'Coordenações'
        unique_together = ('management', 'name')
        ordering = ['name']