"""
Configuración URL dj24

La lista `urlpatterns` enruta las URL a las vistas. Para obtener más información, consulte:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Ejemplos:
Vistas de función
    1. Agregue una importación: desde las vistas de importación de my_app
    2. Agregue una URL a urlpatterns: ruta ('', vistas.inicio, nombre = 'inicio')
Vistas basadas en clases
    1. Agregue una importación: from other_app.views import Home
    2. Agrega una URL a urlpatterns: ruta('', Inicio.as_view(), nombre='inicio')
Incluir otra URLconf
    1. Importe la función include(): desde django.urls import include, ruta
    2. Agrega una URL a urlpatterns: ruta('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
