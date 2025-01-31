# Generated by Django 5.1.5 on 2025-01-31 00:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aid', '0001_initial'),
        ('budgetline', '0009_alter_budgetlinemovement_movement_notes'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='amount_per_installment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor por Parcela'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='assistance_type',
            field=models.CharField(choices=[('UNICO', 'Pagamento Único'), ('PARCELADO', 'Parcelado')], max_length=10, verbose_name='Tipo de Assistência'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='budget_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistances', to='budgetline.budgetline', verbose_name='Linha Orçamentária'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistances', to='employees.employee', verbose_name='Funcionário'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Término'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='installment_count',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de Parcelas'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='start_date',
            field=models.DateField(verbose_name='Data de Início'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando Início'), ('ATIVO', 'Ativo'), ('CONCLUIDO', 'Concluído'), ('CANCELADO', 'Cancelado')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Valor Total'),
        ),
        migrations.AlterField(
            model_name='assistance',
            name='type',
            field=models.CharField(blank=True, choices=[('GRADUACAO', 'Graduação'), ('POS_GRADUACAO', 'Pós-Graduação'), ('AUXILIO_CHECHE_ESCOLA', 'Auxílio Creche Escola'), ('LINGUA_ESTRANGEIRA', 'Língua Estrangeira')], max_length=100, null=True, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='assistanceinstallment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='assistanceinstallment',
            name='assistance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='installments', to='aid.assistance', verbose_name='Assistência'),
        ),
        migrations.AlterField(
            model_name='assistanceinstallment',
            name='due_date',
            field=models.DateField(verbose_name='Data de Vencimento'),
        ),
        migrations.AlterField(
            model_name='assistanceinstallment',
            name='number',
            field=models.PositiveIntegerField(verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='assistanceinstallment',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Pago'),
        ),
        migrations.AlterField(
            model_name='assistanceinstallment',
            name='payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Pagamento'),
        ),
    ]
