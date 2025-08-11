from django.contrib import admin
from django.urls import path, include
# Importe settings e static para servir arquivos de mídia no desenvolvimento
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
path('admin/', admin.site.urls),
path('recipes/', include('recipes.urls')),
]
if settings.DEBUG:
    # Adicione URLs para servir arquivos estáticos e de mídia no modo DEBUG
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)