from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/v1/budgets/', include('budgets.urls')),
    path('api/v1/employees/', include('employees.urls')),
    path('api/v1/sectors/', include('sectors.urls')),
    path('api/v1/centers/', include('centers.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


