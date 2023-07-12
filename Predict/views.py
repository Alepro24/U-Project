from django.shortcuts import render
from App1.models import encuesta,poblacion
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sb
from random import randint, uniform,random

import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.tree import export_graphviz
from sklearn.tree import export_text
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder



# Create your views here.

def prediccion(request):
    #books = encuestaprueba.objects.values_list('Paterno',flat=True)
    #df = pd.DataFrame(list(encuestaprueba.objects.all().values()))
    #Recuperar los datos de algunas columnas en un dataframe
    dframe = pd.DataFrame(list(encuesta.objects.all().values('Edad', 'Sexo','Conocimiento_cereales_a','Consumio_cereales_e','Frecuencia_compra','Marca_cereal_consumo','Consumio_cereales_a','Forma_consumo','Interes_aspectos_nutri','Influencia_compra','Precio_cantidad_apagar','Sabor')))
    dframe.replace({'0': " "})
    dframe.index = np.arange(1, len(dframe)+1)
    mensaje = dframe.to_html(table_id="dtHorizontalVerticalExample",classes="table table-dark",justify="justify-all")
    return render(request,'prediccion.html',{'Mensaje': mensaje})

def prediccionarb(request):
    #books = encuestaprueba.objects.values_list('Paterno',flat=True)
    #df = pd.DataFrame(list(encuestaprueba.objects.all().values()))
    #Recuperar los datos de algunas columnas en un dataframe
    dframe = pd.DataFrame(list(encuesta.objects.all().values('Edad', 'Sexo','Conocimiento_cereales_a','Consumio_cereales_e','Frecuencia_compra','Marca_cereal_consumo','Consumio_cereales_a','Forma_consumo','Interes_aspectos_nutri','Influencia_compra','Precio_cantidad_apagar','Sabor')))
    dframe.replace({'0': " "})
    dframe.index = np.arange(1, len(dframe)+1)
    mensaje = dframe.to_html(table_id="dtHorizontalVerticalExample",classes="table table-dark",justify="justify-all")
    return render(request,'arboldecision.html',{'Mensaje': mensaje})

def rLogistica(areq):
    dfr = pd.DataFrame(list(encuesta.objects.all().values('Edad', 'Sexo','Conocimiento_cereales_a','Consumio_cereales_e','Frecuencia_compra','Marca_cereal_consumo','Consumio_cereales_a','Forma_consumo','Interes_aspectos_nutri','Influencia_compra','Precio_cantidad_apagar','Sabor')))
    df= discredatos(dfr)
    
    dframe = pd.DataFrame(list(encuesta.objects.all().values('Edad', 'Sexo','Conocimiento_cereales_a','Consumio_cereales_e','Frecuencia_compra','Marca_cereal_consumo','Consumio_cereales_a','Forma_consumo','Interes_aspectos_nutri','Influencia_compra','Precio_cantidad_apagar','Sabor')))
    dframe.replace({'0': " "})
    
    
    

    # Algunos datos guardados en variables

    resultados_Sexo=df.groupby('Frecuencia_compra').size()
    fpredicciones = 'hola'
    scoremodelo = 89


    #Crear el modelo

    # Metodo drop para eliminar una columna en este caso "clase" y se guarda en y
    X = np.array(df.drop(['Frecuencia_compra'] , axis='columns'))
    y = np.array(df['Frecuencia_compra'])
    # Se muestra la dimension de x
    X.shape

    #En este caso "x" son las entradas y "y" son las salidas    
    #fit es para ajustar el modelo
    model = linear_model.LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X,y)

    #Clasificar todo nuestro conjunto de entradas X utilizando el método “predict(X)” y ver las primeras 5 predicciones
    predictions = model.predict(X)
    fpredicciones = predictions[0:5]

    #Para ver la precision media de las predicciones del modelo
    scoremodelo=model.score(X,y)
    scoremodelo = round(scoremodelo*100,2)
    scoremod = "%s: %f (%s)" % ('Precisión sin set de prueba',scoremodelo,'%')
    #Validacion del modelo

    #Se debe dividir el dataset a 80% de entrenamiento y 20% de prueba
    validation_size = 0.205
    #La semilla es seed
    seed = 6
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, y, test_size=validation_size, random_state=seed)

    #Se vuelve a correr el modelo pero solo con 80% de datos de entrada y se calcula la presicion
    name='Regresión Logística'
    kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    validacion = msg

    #Ahora si se realiza la prediccion utilizando el conjunto de validacion (el 20% restante)
    predictions = model.predict(X_validation)
    nuevaprecision = accuracy_score(Y_validation, predictions)
    nuevapre=round(nuevaprecision*100,3)

    #Matriz de confusion
    #Muestra cuantos resultados equivocados tuvo de cada clase (los que no están en la diagonal)
    matrizconfusion = confusion_matrix(Y_validation, predictions)
    
   
    mensajedemanda = calculodem(model)

    dframe.index = np.arange(1, len(dframe)+1)
    
    mensaje = dframe.to_html(table_id="dtHorizontalVerticalExample",classes="table table-dark",justify="justify-all")
    return render(areq,'prediccion.html', {'Mensaje': mensaje,'Ndatos':resultados_Sexo,'Score':scoremod,'Matrizlista':(validation_size*100),'Dt':mensajedemanda,'NuevoP':nuevapre,'Matriz':matrizconfusion})

def arbold(request):
    dfr = pd.DataFrame(list(encuesta.objects.all().values('Edad', 'Sexo','Conocimiento_cereales_a','Consumio_cereales_e','Frecuencia_compra','Marca_cereal_consumo','Consumio_cereales_a','Forma_consumo','Interes_aspectos_nutri','Influencia_compra','Precio_cantidad_apagar','Sabor')))
    df= discredatos(dfr)

    dframe = pd.DataFrame(list(encuesta.objects.all().values('Edad', 'Sexo','Conocimiento_cereales_a','Consumio_cereales_e','Frecuencia_compra','Marca_cereal_consumo','Consumio_cereales_a','Forma_consumo','Interes_aspectos_nutri','Influencia_compra','Precio_cantidad_apagar','Sabor')))
   
    
    

    
    X = np.array(df.drop(['Frecuencia_compra'] , axis='columns'))
    y = np.array(df['Frecuencia_compra'])
    
    #Creacion del modelo
    modelo = DecisionTreeClassifier(
            max_depth         = 4,
            criterion         = 'gini',
            random_state      = 6
          )

    modelo.fit(X,y)

    predictions = modelo.predict(X)

    scoremodelo=modelo.score(X,y)
    scoremodelo = round(scoremodelo*100,3)
    scoremod = "%s: %f (%s)" % ('Precisión sin set de prueba',scoremodelo,'%')
    
    
    #Se debe dividir el dataset a 80% de entrenamiento y 20% de prueba
    validation_size = 0.20
    #La semilla es seed
    seed = 6
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=validation_size, random_state=seed)

    #numeric_cols = X_train.select_dtypes(include=['float64', 'int']).columns.to_list()

    predictions = modelo.predict(X_test)
    nuevaprecision = accuracy_score(y_test, predictions)
    
    matrizconfusion = confusion_matrix(y_test, predictions)


    #preprocessor = ColumnTransformer([('onehot', OneHotEncoder(handle_unknown='ignore'), numeric_cols)],remainder='passthrough')

    #X_train_prep = preprocessor.fit_transform(X_train)
    #X_test_prep  = preprocessor.transform(X_test)

    # Convertir el output del ColumnTransformer en dataframe y añadir el nombre de las columnas
    # ------------------------------------------------------------------------------
    # Nombre de todas las columnas
    #encoded_cat = preprocessor.named_transformers_['onehot'].get_feature_names(numeric_cols)
    #labels = np.concatenate([numeric_cols, encoded_cat])

    # Conversión a dataframe
    #X_train_prep = pd.DataFrame(X_train_prep, columns=labels)
    #X_test_prep  = pd.DataFrame(X_test_prep, columns=labels)
    #X_train_prep.info()

    
    # Entrenamiento del modelo
    # ------------------------------------------------------------------------------
    modelo.fit(X_train, y_train)


    # Estructura del árbol creado
    # ------------------------------------------------------------------------------
    #fig, ax = plt.subplots(figsize=(13, 6))

    profundidad = (f"Profundidad del árbol: {modelo.get_depth()}")
    nodosterminales = (f"Número de nodos terminales: {modelo.get_n_leaves()}")

    #plot = plot_tree(
                #decision_tree = modelo,
                #feature_names = labels.tolist(),
                #class_names   = 'Frecuencia_compra',
                #filled        = True,
                #impurity      = False,
                #fontsize      = 7,
                #ax            = ax
        #)

    # Error de test del modelo
    #-------------------------------------------------------------------------------
    predicciones = modelo.predict(X = X_test)

    
    matrizconfusion = confusion_matrix(
        y_true    = y_test,
        y_pred    = predicciones
    )


    accuracy = accuracy_score(
                y_true    = y_test,
                y_pred    = predicciones,
                normalize = True
            )
    precision = (f"Precisión con set de prueba: {100 * accuracy} %")


    
    mensajedemanda = calculodem(modelo)
    
    
    dframe.index = np.arange(1, len(dframe)+1)
    mensaje = dframe.to_html(table_id="dtHorizontalVerticalExample",classes="table table-dark",justify="justify-all")
    
    return render(request,'arboldecision.html', {'Mensaje': mensaje,'Profundidad': profundidad,'Ndatos':scoremod, 'Score':precision,'Matriz': matrizconfusion,'Dt':mensajedemanda})

def discredatos(dff):
    df = dff
    
    # Discretizacion de datos

    df.Sexo[df.Sexo=='Mujer'] = '0'
    df.Sexo[df.Sexo=='Hombre'] = '1'

    df.Conocimiento_cereales_a[df.Conocimiento_cereales_a=='Sí']='1'
    df.Conocimiento_cereales_a[df.Conocimiento_cereales_a=='No']='0'

    df.Consumio_cereales_e[df.Consumio_cereales_e=='Sí']='1'
    df.Consumio_cereales_e[df.Consumio_cereales_e=='No']='0'
    
    df.Frecuencia_compra[df.Frecuencia_compra=='Una vez a la semana']='1'
    df.Frecuencia_compra[df.Frecuencia_compra=='Cada dos veces al mes']='2'
    df.Frecuencia_compra[df.Frecuencia_compra=='Una vez al mes']='3'
    df.Frecuencia_compra[df.Frecuencia_compra=='Cada dos meses']='4'
    df.Frecuencia_compra[df.Frecuencia_compra=='Cada tres meses']='5'
    

    df.Marca_cereal_consumo[df.Marca_cereal_consumo=="Kellogg's"]='1'
    df.Marca_cereal_consumo[df.Marca_cereal_consumo=='Nestle']='2'
    df.Marca_cereal_consumo[df.Marca_cereal_consumo=='KRIS']='3'
    df.Marca_cereal_consumo[df.Marca_cereal_consumo=='Princesa']='4'
    df.Marca_cereal_consumo[df.Marca_cereal_consumo=='Irupana']='5'
    df.Marca_cereal_consumo[df.Marca_cereal_consumo=='Otros']='6'


    df.Consumio_cereales_a[df.Consumio_cereales_a=='Si']='1'
    df.Consumio_cereales_a[df.Consumio_cereales_a=='No']='2'


    df.Forma_consumo[df.Forma_consumo=='Barra energetica']='1'
    df.Forma_consumo[df.Forma_consumo=='Hojuelas']='2'
    df.Forma_consumo[df.Forma_consumo=='Polvo']='3'
    df.Forma_consumo[df.Forma_consumo=='Todas']='4'
    df.Forma_consumo[df.Forma_consumo=='Ninguna']='5'

    df.Interes_aspectos_nutri[df.Interes_aspectos_nutri=='Sí']='1'
    df.Interes_aspectos_nutri[df.Interes_aspectos_nutri=='No']='2'

    df.Influencia_compra[df.Influencia_compra=='Datos Nutricionales']='1'
    df.Influencia_compra[df.Influencia_compra=='Composición']='2'
    df.Influencia_compra[df.Influencia_compra=='Presentación']='3'
    df.Influencia_compra[df.Influencia_compra=='Precio']='4'
    df.Influencia_compra[df.Influencia_compra=='Sabor']='5'
    df.Influencia_compra[df.Influencia_compra=='Datos Nutricionales, Composición']='6'
    df.Influencia_compra[df.Influencia_compra=='Precio, Sabor']='7'
    df.Influencia_compra[df.Influencia_compra=='Precio, Sabor, Datos Nutricionales']='8'
    df.Influencia_compra[df.Influencia_compra=='Precio, Sabor, Presentación']='9'
    df.Influencia_compra[df.Influencia_compra=='Sabor, Datos Nutricionales']='10'

    df.Precio_cantidad_apagar[df.Precio_cantidad_apagar=='Menos de 20 Bs (Peso 120 g)']='1'
    df.Precio_cantidad_apagar[df.Precio_cantidad_apagar=='Entre 20 - 25 Bs (Peso 160 g)']='2'
    df.Precio_cantidad_apagar[df.Precio_cantidad_apagar=='Entre 26 - 30 Bs (Peso 270 g)']='3'
    df.Precio_cantidad_apagar[df.Precio_cantidad_apagar=='Entre 31 - 35 Bs (Peso 420 g)']='4'
    df.Precio_cantidad_apagar[df.Precio_cantidad_apagar=='Entre 36 - 40 Bs (Peso 500 g)']='5'
    df.Precio_cantidad_apagar[df.Precio_cantidad_apagar=='Mas de 40 Bs (Peso 730 g)']='6'
    
    df.Sabor[df.Sabor=='Original']='1'
    df.Sabor[df.Sabor=='Chocolate']='2'
    df.Sabor[df.Sabor=='Naranja']='3'
    df.Sabor[df.Sabor=='Frutilla']='4'
    df.Sabor[df.Sabor=='Vainilla']='5'
    df.Sabor[df.Sabor=='Otros']='6'

    return df
    
def calculodem(mod):
    
    dfpob= pd.DataFrame(list(poblacion.objects.all().values('Mercado_objetivo')))
    lpobla =[]
    for i in [1,2,3,4,5,6,7,8,9,10]:
        lpobla.append(dfpob.iloc[i]['Mercado_objetivo'])
    demandakg = []
    for ap in [0,1,2,3,4,5,6,7,8,9]:
        matrizdemanda =0
        mat = np.array([200,2])
        listav=[]
        lmp =[]
        lmo =[]
        for i in range(196):
            variablecant = randint(1,6)
            vmp = randint(0,2)
            vmo = randint(0,1)
            X_new = pd.DataFrame(
                {'Edad':[randint(20,64)], 
                'Sexo':[randint(0,1)],
                'Conocimiento_cereales_a':[randint(0,1)],
                'Consumio_cereales_e':[vmo],
                'Marca_cereal_consumo':[randint(1,6)],
                'Consumio_cereales_a':[vmp],
                'Forma_consumo':[randint(1,5)],
                'Interes_aspectos_nutri':[randint(1,2)],
                'Influencia_compra':[randint(1,10)],
                'Precio_cantidad_apagar':[variablecant],
                'Sabor':[randint(1,6)]}
            )
            prediccionmodelo = mod.predict(X_new)
            frecompra = int(prediccionmodelo[0])
            parelementos=[variablecant,frecompra]
            listav.append(parelementos)
            lmp.append(vmp)
            lmo.append(vmo)
            #np.insert(mat,i,parelementos)
        
        pmp = round((lmp.count(1) / 196) , 2)
        pmo = round((lmo.count(1)/ 196),2)
        
        frame=np.array(listav)
        hola =0
        listaval =[]
        contceros = 0
        for j in [0,1,2,3,4,5]:
            contc = listav.count([0,j])
            contceros = contceros + contc
        for i in [0,1,2,3,4,5,6]:
            contc = listav.count([i,0])
            contceros = contceros + contc
        numero = 195-contceros
        for i in [1,2,3,4,5,6]:
            for j in [1,2,3,4,5]:
                hola = listav.count([i,j])
                v = hola/numero
                w=round(v,4)
                listaval.append(w)
        lis = []
        vcantp = 0
        lpoblacion = [281398,283488,285593,287714,289851,292004,294172,296357,298558,300775,303009]
        
        vpmp = int(lpoblacion[ap])
        vpmo = int(vpmp*1)

        for l in range(30):
            
            vcantp = ((listaval[l])*vpmo)
            r = round(vcantp,2)
            lis.append(r)
        sumalis = sum(lis)
        lisaux = []
        t=0
        for u in [0,1,2,3,4,5]:
            if (u==1):
                t=5
            if (u==2):
                t=10
            if (u==3):
                t=15
            if (u==4):
                t=20
            if (u==5):
                t=25
            vg = (lis[t]*4 + lis[t+1]*2 + lis[t+2] + lis[t+3]/2 + lis[t+4]/3)
            s = int(vg)
            lisaux.append(s)
        listadcantmesg=[]
        listadcantmeskg=[]
        listadcantanno=[]
        a=120
        for p in [0,1,2,3,4,5]:
            if (p==1):
                a=160
            if (p==2):
                a=270
            if (p==3):
                a=420
            if (p==4):
                a=500
            if (p==5):
                a=730
            listadcantmesg.append(lisaux[p]*a)
            listadcantmeskg.append(listadcantmesg[p]/1000)
            listadcantanno.append(listadcantmeskg[p]*12)
        
        demandakg.append(round(sum(listadcantanno),2))
        #consumopercapita = demandakg / (sum(lisaux))


    
    
    dfdemanda = DataFrame(demandakg,columns=['Demanda en Kg'])
    dfdemanda.insert(0,"Año",['2021','2022','2023','2024','2025','2026','2027','2028','2029','2030'],True)
    cols = ['Demanda en Kg'] 
    dfdemanda[cols] = dfdemanda[cols].applymap("{:,}".format)
    dfdemanda.index = np.arange(1, len(dfdemanda)+1)
    mensajedemanda = dfdemanda.to_html(table_id="dtHorizontalVerticalExample",classes="table table-dark",justify="justify-all")

    return mensajedemanda
    