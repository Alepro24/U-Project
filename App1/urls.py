from django.urls import path
from App1 import views

urlpatterns = [
    path('index',views.home, name="Home"),
    path('datos',views.datos, name="Datos"),
    path('modelos',views.modelos, name="Modelos"),
    path('graficos',views.graficos, name="Graficos"),
    path('mapa',views.mapa, name="Mapa"),
    path('principal',views.principal, name="Principal"),
    path('entrenamiento',views.entrenamiento, name="Entrenamiento"),
    path('encuesta',views.encuesta, name="Encuesta"),
    path('mapa',views.mapa, name="Mapa"),
    path('subirEncuesta',views.subirEncuesta, name="subirEncuesta"),
    path('ingresarDato',views.ingresarDato, name="ingresarDato"),
    path('subirProducto',views.subirProducto, name="subirProducto"),
    path('subirPoblacion',views.subirPoblacion, name="subirPoblacion"),
    path('subirCereal',views.subirCereal, name="subirCereal"),
    path('subirDgeneral',views.subirDgeneral, name="subirDgeneral"),
    path('graficospro',views.graficospro, name="graficospro"),
    path('datoss',views.graficospro, name="graficospro"),
    
]