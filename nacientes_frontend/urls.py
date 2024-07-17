from django.urls import path
from . import views

app_name = 'nacientes_frontend'
urlpatterns = [
    path("", views.nacientesListaMapa, name='nacientes-lista-mapa')
]