from django.shortcuts import render, HttpResponse
import pandas as pd
import numpy as np
import csv
from django.conf import settings
from sqlalchemy.engine import create_engine
from App1.models import encuestaprueba, productos, cereal, poblacion,dgeneral, cantcultivada
from AppLogin.models import Usuario
from pandas import isnull
from django.views.decorators.cache import never_cache



# Create your views here.

#Home
def home(request):
    #Tabla poblacion
    dfpoblacion = pd.DataFrame(list(poblacion.objects.all().values('Localidad','Anno','Pet','Pea','Poblacion_segmentada','Mercado_potencial','Mercado_objetivo')))
    cols = ['Pet', 'Pea','Poblacion_segmentada','Mercado_potencial','Mercado_objetivo'] 
    dfpoblacion[cols] = dfpoblacion[cols].applymap("{:,}".format)
    if dfpoblacion.empty:
        tpoblacion="Tabla vacia"
    else:
        dfpoblacion.index = np.arange(1, len(dfpoblacion)+1)
        tpoblacion = dfpoblacion.to_html(classes="table table-striped table-bordered",justify="justify-all")
    return render(request,"index.html",{"Tpoblacion":tpoblacion})

#Datos
def datos(request):
    return render(request,"datos.html")

#Modelos
def modelos(request):
    return render(request,"modelos.html")

#Gráficos
def graficos(request):
    return render(request,"graficos.html")

#Mapa
def mapa(request):
    
    dfproducto = pd.DataFrame(list(cantcultivada.objects.all().values('Provincia','Quinua','Cebada','Canahua')))
    if dfproducto.empty:
        tcereales="Tabla vacia"
    else:
        dfproducto.index = np.arange(1, len(dfproducto)+1)
        tcereales = dfproducto.to_html(classes="table table-striped table-bordered",justify="justify-all")
    
    return render(request,"mapa.html",{"Tcereal":tcereales})

def principal(request):
    return render(request,"principal.html")

def entrenamiento(request):
    #Tabla producto
    dfproducto = pd.DataFrame(list(productos.objects.all().values('Nombre','Descripcion')))
    if dfproducto.empty:
        tproducto="Tabla vacia"
    else:
        dfproducto.index = np.arange(1, len(dfproducto)+1)
        tproducto = dfproducto.to_html(classes="table table-striped table-bordered",justify="justify-all")
    #Tabla cereal
    dfcereal = pd.DataFrame(list(cereal.objects.all().values('Nombre','Clase')))
    if dfcereal.empty:
        tcereal="Tabla vacia"
    else:
        dfcereal.index = np.arange(1, len(dfcereal)+1)
        tcereal = dfcereal.to_html(classes="table table-dark",justify="justify-all")
    #Tabla poblacion
    dfpoblacion = pd.DataFrame(list(poblacion.objects.all().values('Localidad','Anno','Pet','Pea','Poblacion_segmentada','Mercado_potencial','Mercado_objetivo')))
    cols = ['Pet', 'Pea','Poblacion_segmentada','Mercado_potencial','Mercado_objetivo'] 
    dfpoblacion[cols] = dfpoblacion[cols].applymap("{:,}".format)

    if dfpoblacion.empty:
        tpoblacion="Tabla vacia"
    else:
        dfpoblacion.index = np.arange(1, len(dfpoblacion)+1)
        tpoblacion = dfpoblacion.to_html(classes="table table-striped table-bordered",justify="justify-all")
    #Tabla datos generales
    dfdgeneral = pd.DataFrame(list(dgeneral.objects.all().values('Anno','Lugar','Superficie','Produccion','Rendimiento','Cant_exportacion')))
    if dfdgeneral.empty:
        tdgeneral="Tabla vacia"
    else:
        dfdgeneral.index = np.arange(1, len(dfdgeneral)+1)
        tdgeneral = dfdgeneral.to_html(classes="table table-bordered table-dark",justify="justify-all")

    return render(request,"entrenamiento.html",{"Tproducto":tproducto,"Tcereal":tcereal,"Tpoblacion":tpoblacion,"Tdgeneral":tdgeneral})

def encuesta(request):
    return render(request,"encuesta.html")

def subirEncuesta(request):
    if request.method=="POST":
        if request.FILES.get('archivocsv'):
            archivocsv=request.FILES["archivocsv"]
            df = pd.read_csv(archivocsv)
            df=df.applymap(lambda x: '0' if isnull(x) else x)
            if archivocsv:
                df.index = np.arange(1, len(df)+1)
                mensaje= df.to_html(table_id="dtHorizontalVerticalExample",classes="table table-bordered table-striped mb-0",justify="justify-all")
                user = settings.DATABASES['default']['USER']
                password = settings.DATABASES['default']['PASSWORD']
                database_name = settings.DATABASES['default']['NAME']

                database_url = 'mysql://{user}:{password}@localhost:5432/{database_name}'.format(
                    user=user,
                    password=password,
                    database_name=database_name,
                )

                engine = create_engine(database_url, echo=False)
                df.to_sql('App1_encuesta', con=engine, if_exists='replace',index=False)

                return render(request,"encuesta.html",{"Mensaje": mensaje})
            else:
                mensaje= "Solo se aceptan archivos csv"
                return render(request,"encuesta.html",{"Mensaje": mensaje})
        else:
            mensaje= "Seleccione un archivo"
            return render(request,"encuesta.html",{"Mensaje": mensaje})
    else:
        mensaje= "Error de carga de archivo"
        return render(request,"encuesta.html",{"Mensaje": mensaje})


def ingresarDato(request):
    return render(request,"ingresardatos.html")

def subirProducto(request):
    if request.POST["producto"]:
        productoo=request.POST["producto"]
        descripcion = request.POST["descripcion"]

        # armar la lista de datos
        u = Usuario(Nro_Usuario=1)

        prod = productos()
        prod.Nombre = productoo
        prod.Descripcion = descripcion
        prod.Nro_Usuario = u
        prod.Estado = 1
        prod.save()
        
        return render(request,"ingresardatos.html")
    else:
        mensaje= "Error de carga de archivo"
        return render(request,"ingresardatos.html",{'Mensaje':mensaje})


def subirPoblacion(request):
    if request.method=="POST":
        if request.FILES.get('archivocsv'):
            archivocsv=request.FILES["archivocsv"]
            df = pd.read_csv(archivocsv)
            #df=df.applymap(lambda x: '0' if isnull(x) else x)
            if archivocsv:
                df.index = np.arange(1, len(df)+1)
                mensaje= df.to_html(table_id="dtHorizontalVerticalExample",classes="table table-bordered table-striped mb-0",justify="justify-all",columns=['Localidad','Anno','Pet','Pea','Poblacion_segmentada','Mercado_potencial','Mercado_objetivo'])
                user = settings.DATABASES['default']['USER']
                password = settings.DATABASES['default']['PASSWORD']
                database_name = settings.DATABASES['default']['NAME']
                
                database_url = 'mysql://{user}:{password}@localhost:5432/{database_name}'.format(
                    user=user,
                    password=password,
                    database_name=database_name,
                )

                engine = create_engine(database_url, echo=False)
                df.to_sql('App1_poblacion', con=engine, if_exists='replace',index=False)

                return render(request,"encuesta.html",{"Mensaje": mensaje})
            else:
                mensaje= "Solo se aceptan archivos csv"
                return render(request,"encuesta.html",{"Mensaje": mensaje})
        else:
            mensaje= "Seleccione un archivo"
            return render(request,"encuesta.html",{"Mensaje": mensaje})
    else:
        mensaje= "Error de carga de archivo"
        return render(request,"encuesta.html",{"Mensaje": mensaje})

def subirCereal(request):
    if request.POST["cereal"]:
        cereall=request.POST["cereal"]
        clase = request.POST["clase"]

        # armar la lista de datos
        u = Usuario(Nro_Usuario=1)

        cere = cereal()
        cere.Nombre = cereall
        cere.Clase = clase
        cere.Nro_Usuario = u
        cere.Estado = 1
        cere.save()
        
        return render(request,"ingresardatos.html")
    else:
        mensaje= "Error de carga de archivo"
        return render(request,"ingresardatos.html",{'Mensaje':mensaje})

def subirDgeneral(request):
    if request.method=="POST":
        if request.FILES.get('archivocsv'):
            archivocsv=request.FILES["archivocsv"]
            df = pd.read_csv(archivocsv)
            #df=df.applymap(lambda x: '0' if isnull(x) else x)
            if archivocsv:
                mensaje= df.to_html()
                user = settings.DATABASES['default']['USER']
                password = settings.DATABASES['default']['PASSWORD']
                database_name = settings.DATABASES['default']['NAME']

                database_url = 'mysql://{user}:{password}@localhost:5432/{database_name}'.format(
                    user=user,
                    password=password,
                    database_name=database_name,
                )

                engine = create_engine(database_url, echo=False)
                df.to_sql('App1_dgeneral', con=engine, if_exists='replace',index=False)

                return render(request,"encuesta.html",{"Mensaje": mensaje})
            else:
                mensaje= "Solo se aceptan archivos csv"
                return render(request,"encuesta.html",{"Mensaje": mensaje})
        else:
            mensaje= "Seleccione un archivo"
            return render(request,"encuesta.html",{"Mensaje": mensaje})
    else:
        mensaje= "Error de carga de archivo"
        return render(request,"encuesta.html",{"Mensaje": mensaje})

@never_cache
def graficospro(request):
    listavar = []
    for i in [ 67, 15, 35,25, 8 ]:
        listavar.append(i)
    return render(request,"graficosproyecto.html",{"myvar":listavar})

