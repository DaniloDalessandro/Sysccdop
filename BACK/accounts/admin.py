from django.contrib import admin

from accounts.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar', 'name', 'email', 'last_access')
    readonly_fields = ('last_access',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields
        return []

admin.site.register(User, UserAdmin)

admin.site.site_header = "Painel Administrativo"
admin.site.site_title = "Administração do Sistema"
admin.site.index_title = "Bem-vindo ao Painel de Administração"
