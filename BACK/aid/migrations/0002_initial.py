# Generated by Django 5.1.5 on 2025-02-04 23:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aid', '0001_initial'),
        ('budgetline', '0001_initial'),
        ('employees', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='assistance',
            name='budget_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistances', to='budgetline.budgetline', verbose_name='Linha Orçamentária'),
        ),
        migrations.AddField(
            model_name='assistance',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_assistances', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='assistance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistances', to='employees.employee', verbose_name='Funcionário'),
        ),
        migrations.AddField(
            model_name='assistance',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_assistances', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
    ]
