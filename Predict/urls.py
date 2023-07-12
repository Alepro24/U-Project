from django.urls import path
from Predict import views

urlpatterns = [
    path('prediccion',views.prediccion, name="Prediccion"),
    path('prediccionarb',views.prediccionarb, name="prediccionarb"),
    path('rLogistica',views.rLogistica, name="rLogistica"),
    path('arbold',views.arbold, name="arbold"),
]