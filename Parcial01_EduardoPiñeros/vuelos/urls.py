from django.urls import path
from .views import InitialView,RegistrarView,ListarView,EstadisticaView

urlpatterns = [
    path("",InitialView.as_view(),name='initial_view'),
    path("registar/",RegistrarView.as_view(),name='registrar'),
    path("listar/",ListarView.as_view(),name='listar'),
    path("estadisticas/",EstadisticaView.as_view(),name='estadistica')
]