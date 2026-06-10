from django.contrib import admin
from django.urls import path
from .views import homepage  # Importa a lógica que puxa os tópicos

urlpatterns = [
    path('admin/', admin.site.get_urls() if hasattr(admin.site, 'get_urls') else admin.site.urls),
    path('', homepage, name='home'),  # Abre a vitrine escura diretamente na raiz do site
]