# Generated by Django 5.1.5 on 2025-01-30 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgetline', '0007_alter_budgetlinemovement_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgetlinemovement',
            options={'ordering': ['-created_at'], 'verbose_name': 'Movimentação', 'verbose_name_plural': 'Movimentações'},
        ),
        migrations.RemoveField(
            model_name='budgetlinemovement',
            name='movement_date',
        ),
    ]
