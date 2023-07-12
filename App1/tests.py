from django.test import TestCase
from App1.views import entrenamiento
from App1 import views
from App1.urls import path
from App1.models import productos,poblacion,cereal,encuesta
from AppLogin.models import Usuario
import pandas as pd
from pandas import DataFrame
# Create your tests here.

class Pruebasapp1(TestCase):

    def test_home_page_codigo_estado(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_vista_index(self):
        response = self.client.get('/index')
        self.assertEquals(response.status_code, 200)
    
    def test_pagina_index_html(self):
        response = self.client.get('/index')
        self.assertContains(response, '<div class="stat-heading">Producción</div>')

    def test_vista_principal_html(self):
        response = self.client.get('/principal')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'principal.html')
    
    def test_pagina_principal_contiene_codigo(self):
        response = self.client.get('/principal')
        self.assertContains(response, '<h1 class="pb-2 display-4" style="text-align: center;">Machine Learning</h1>')

    def test_ingresar_productos(self):
        Usuario.objects.create(Usuario='Ale',Estado=1)
        user_pk = Usuario.objects.get(Usuario='Ale').Nro_Usuario
        est = Usuario.objects.get(Usuario='Ale').Estado
        data1 = {
            "producto": "Proti-Mixx",
            "descripcion": "Cereal-hojuelas",
            "Nro_Usuario":user_pk,
            "Estado": est ,
        }
        response = self.client.post("/subirProducto", data=data1, secure='csrf_token')
        self.assertEquals(response.status_code, 200)
    
    def test_ingresar_poblacion(self):
        
        datos = {
        "Localidad":'La Paz',
        "Anno":2021,
        "Pet":232323,
        "Pea":12121,
        "Poblacion_segmentada":5903,
        "Mercado_potencial":4129,
        "Mercado_objetivo":3928,
        "Estado":True
        }
        response = self.client.post("/subirPoblación", data=datos, secure='csrf_token')
        self.assertEquals(response.status_code, 404)
    
    def test_ingresar_datosgenerales(self):
        dt = pd.DataFrame()
        response = self.client.post("/subirDgeneral",data=dt)
        self.assertEquals(response.status_code, 200)

    def test_datos_contiene_tablas(self):
        response = self.client.get('/entrenamiento')
        self.assertContains(response, '<strong class="card-title">Tabla Población</strong>')
    
    def test_carga_tablas_con_datos(self):
        df = pd.DataFrame()
        response = self.client.get('/entrenamiento',data=df)
        self.assertEquals(response.status_code, 200)

    def test_carga_encuesta(self):
        df = pd.DataFrame()
        response = self.client.post('/subirEncuesta',data=df)
        self.assertEquals(response.status_code, 200)
    
    def test_vista_graficos(self):
        response = self.client.get('/graficospro')
        self.assertEquals(response.status_code, 200)

    def test_pagina_graficos_html_correcto(self):
        response = self.client.get('/graficospro')
        self.assertContains(response, '<canvas id="polarChart"></canvas>')
        self.assertContains(response, '<canvas id="sales-chart"></canvas>')
        self.assertContains(response, '<canvas id="team-chart"></canvas>')
        self.assertContains(response, '<canvas id="barChart"></canvas>')
        self.assertContains(response, '<canvas id="lineChart"></canvas>')

    def test_pagina_graficos_html_incorrecto(self):
        response = self.client.get('/graficospro')
        self.assertNotContains(response, '<canvas id="GraficoPolar"></canvas>')


