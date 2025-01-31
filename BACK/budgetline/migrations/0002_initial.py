# Generated by Django 5.1.5 on 2025-01-29 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budgetline', '0001_initial'),
        ('budgets', '0001_initial'),
        ('centers', '0004_alter_management_center_options_and_more'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetline',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='budget_lines', to='budgets.budget'),
        ),
        migrations.AddField(
            model_name='budgetline',
            name='managing_cost_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='budget_lines', to='centers.management_center'),
        ),
        migrations.AddField(
            model_name='budgetline',
            name='possible_fiscal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='possible_contract_fiscal', to='employees.employee', verbose_name='Fiscal'),
        ),
        migrations.AddField(
            model_name='budgetline',
            name='requesting_cost_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='centers.requesting_center'),
        ),
    ]
