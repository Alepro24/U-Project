from django.test import TestCase
import pandas as pd
from App1.models import encuesta,poblacion
from Predict.views import discredatos,calculodem
from sklearn import linear_model

# Create your tests here.

class PruebasModelos(TestCase):
    
    def test_funcion_dicredatos(self):
        response = self.client.get(discredatos)
        self.assertEquals(response.status_code, 404)
    
    def test_vista_url_prediccion(self):
        response = self.client.get('/prediccion')
        self.assertEquals(response.status_code, 200)

    def test_vista_template_correcto(self):
        response = self.client.get('/prediccionarb')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'arboldecision.html')
        