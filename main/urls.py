
from django.contrib import admin
from django.urls import path
from reservas.views import index, cadastrar_reserva,listar_reservas, mais, detalhar, apagar, editar, sobre
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('form/', cadastrar_reserva,name='cadastrar'),
    path('listar/', listar_reservas,name='listar'),
    path('mais/',mais, name='mais'),
    path('detalhe/<int:id>/', detalhar, name='detalhar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('apagar/<int:id>/', apagar, name='apagar'),
    path('sobre_nos/', sobre, name='sobre'),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)