from django.contrib import admin

from accounts.models import User

admin.site.register(User)

admin.site.site_header = 'SysContracts'