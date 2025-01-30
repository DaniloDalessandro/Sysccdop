from django.contrib import admin

from accounts.models import User

admin.site.register(User)

admin.site.site_header = "Painel Administrativo"
admin.site.site_title = "Administração do Sistema"
admin.site.index_title = "Bem-vindo ao Painel de Administração"
