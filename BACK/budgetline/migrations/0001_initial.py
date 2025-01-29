# Generated by Django 5.1.5 on 2025-01-29 19:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('CAPEX', 'CAPEX'), ('OPEX', 'OPEX')], max_length=100, null=True, verbose_name='Budget Type')),
                ('expense_type', models.CharField(choices=[('Base Principal', 'Base Principal'), ('Serviços Especializados', 'Serviços Especializados'), ('Despesas Compartilhadas', 'Despesas Compartilhadas')], max_length=100, verbose_name='Expense Type')),
                ('summary_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição resumida')),
                ('object', models.CharField(blank=True, max_length=80, null=True, verbose_name='Object')),
                ('budget_classification', models.CharField(blank=True, choices=[('NOVO', 'NOVO'), ('RENOVAÇÃO', 'RENOVAÇÃO'), ('CARY OVER', 'CARY OVER'), ('REPLANEJAMENTO', 'REPLANEJAMENTO'), ('N/A', 'N/A')], max_length=100, null=True)),
                ('contract_type', models.CharField(blank=True, choices=[('SERVIÇO', 'SERVIÇO'), ('FORNECIMENTO', 'FORNECIMENTO'), ('ASSINATURA', 'ASSINATURA'), ('FORNECIMENTO/SERVIÇO', 'FORNECIMENTO/SERVIÇO')], max_length=100, null=True)),
                ('probable_procurement_type', models.CharField(choices=[('LICITAÇÃO', 'LICITAÇÃO'), ('DISPENSA EM RAZÃO DO VALOR', 'DISPENSA EM RAZÃO DO VALOR'), ('CONVÊNIO', 'CONVÊNIO'), ('FUNDO FIXO', 'FUNDO FIXO'), ('INEXIGIBILIDADE', 'INEXIGIBILIDADE'), ('ATA DE REGISTRO DE PREÇO', 'ATA DE REGISTRO DE PREÇO'), ('ACORDO DE COOPERAÇÃO', 'ACORDO DE COOPERAÇÃO'), ('APOSTILAMENTO', 'APOSTILAMENTO')], max_length=100)),
                ('budgeted_amount', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('process_status', models.CharField(blank=True, choices=[('VENCIDO', 'VENCIDO'), ('DENTRO DO PRAZO', 'DENTRO DO PRAZO'), ('ELABORADO COM ATRASO', 'ELABORADO COM ATRASO'), ('ELABORADO NO PRAZO', 'ELABORADO NO PRAZO')], max_length=100, null=True)),
                ('contract_status', models.CharField(blank=True, choices=[('DENTRO DO PRAZO', 'DENTRO DO PRAZO'), ('CONTRATADO NO PRAZO', 'CONTRATADO NO PRAZO'), ('CONTRATADO COM ATRASO', 'CONTRATADO COM ATRASO'), ('PRAZO VENCIDO', 'PRAZO VENCIDO'), ('LINHA TOTALMENTE REMANEJADA', 'LINHA TOTALMENTE REMANEJADA'), ('LINHA TOTALMENTE EXECUTADA', 'LINHA TOTALMENTE EXECUTADA'), ('LINHA DE PAGAMENTO', 'LINHA DE PAGAMENTO'), ('LINHA PARCIALMENTE REMANEJADA', 'LINHA PARCIALMENTE REMANEJADA'), ('LINHA PARCIALMENTE EXECUTADA', 'LINHA PARCIALMENTE EXECUTADA'), ('N/A', 'N/A')], max_length=100, null=True)),
                ('contract_notes', models.TextField(blank=True, max_length=400, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Linha Orçamentária',
                'verbose_name_plural': 'Linhas Orçamentárias',
            },
        ),
    ]
