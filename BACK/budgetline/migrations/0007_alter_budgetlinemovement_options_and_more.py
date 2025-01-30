# Generated by Django 5.1.5 on 2025-01-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetline', '0006_alter_budgetline_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgetlinemovement',
            options={'ordering': ['-movement_date'], 'verbose_name': 'Movimentação', 'verbose_name_plural': 'Movimentações'},
        ),
        migrations.AlterField(
            model_name='budgetlinemovement',
            name='movement_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da Movimentação'),
        ),
    ]
