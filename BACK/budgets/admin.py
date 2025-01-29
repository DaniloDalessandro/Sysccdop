from django.contrib import admin

from budgets.models import Budget,BudgetMovement

# Register your models here.
admin.site.register(Budget)
admin.site.register(BudgetMovement)