# Generated by Django 5.1.5 on 2025-02-05 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetline', '0002_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetline',
            name='possible_fiscal',
        ),
        migrations.AddField(
            model_name='budgetline',
            name='main_fiscal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='main_contract_fiscal', to='employees.employee', verbose_name='Fiscal Principal'),
        ),
        migrations.AddField(
            model_name='budgetline',
            name='secondary_fiscal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='secondary_contract_fiscal', to='employees.employee', verbose_name='Fiscal Substituto'),
        ),
    ]
