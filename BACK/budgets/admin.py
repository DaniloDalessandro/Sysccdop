from django.contrib import admin

from budgets.models import Budget,BudgetMovement

#=================================================================================================================

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('year', 'category', 'management_center', 'total_amount', 'available_amount', 'created_by', 'updated_by', 'created_at', 'updated_at')  
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')  

    def save_model(self, request, obj, form, change):
        
        if not obj.pk: 
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Budget, BudgetAdmin)

#=================================================================================================================

class BudgetMovementAdmin(admin.ModelAdmin):
    list_display = ('source', 'destination', 'amount', 'movement_date', 'notes', 'created_by', 'updated_by', 'created_at', 'update_at')  
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'update_at')  

    def save_model(self, request, obj, form, change):
        
        if not obj.pk: 
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(BudgetMovement, BudgetMovementAdmin)