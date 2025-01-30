from django.contrib import admin
from .models import Requesting_Center, Management_Center

#=================================================================================================================

class RequestingCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','created_by', 'updated_by', 'created_at', 'updated_at')  
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')  

    def save_model(self, request, obj, form, change):
        
        if not obj.pk: 
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Requesting_Center, RequestingCenterAdmin)


#=================================================================================================================

class ManagementCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','created_by', 'updated_by', 'created_at', 'updated_at')  
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')  
    search_fields = ('name',)
    list_filter = ('name',)    

    def save_model(self, request, obj, form, change):
        
        if not obj.pk: 
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Management_Center, ManagementCenterAdmin)