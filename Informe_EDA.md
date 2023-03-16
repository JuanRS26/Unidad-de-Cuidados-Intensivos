
<h1 align="center">
<b>INFORME: ANALISIS EDA DATAFRAMES 
UNIDAD DE CUIDADOS INTENSIVOS MIMIC-III<b>
</h1>

<b>*A continuación se resume el Análisis Exploratorio de Datos (EDA) para cada una de las 26 tablas.correspondiente al MIMIC-III “Medical Information Mart for Intensive Care”. MIMIC-III es una colección completa de datos sin identificación de 53.423 ingresos hospitalarios de cuidados intensivos distintos de 38.597 adultos distintos pacientes en el Centro Médico Beth Israel Deaconess en Boston, Massachusetts.*</b> 


**1. Dataframe CALLOUT.csv**
77 Filas
24 Columnas
18 Catergoricas
6 Numericas

Las variables necesitan Transformaciones: 
'submit_careunit'(88% NaN)
'firstreservationtime' (49% NaN)
'currentreservationtime' (94% NaN)
Las culmunas con Datos de Fecha estan encripatadas con valores de año cambiados (años entre el 2100-2200).

**2. Dataframe 'SERVICES.cvs'**

163 filas
6 columnas
3 numericcas 
3 categoricas

Las Variables que necesitan trasformaciones:
'prev_service' (79%  NaN)

**3.Dataframe 'DRGCODES.csv'**
297 filas
8 coumnas
4 numericas
4 catergoricas
Las variables que necesitan Transformaciones: 
'dgr_mortality' (43% NaN)
'dgr_severity' (43% NaN)

**4. Dataframe 'CPTEVENTS.csv'**
1579 filas 
12 Columnas
6 Numericas
6 Categoricas
Las Variables que necesitan transformaciones. 
'chardate' (82% NaN)
'cpt_suffix' (100% NaN)

**5. Dataframe 'DIAGNOSES_ICD.csv'**
1761 filas 
5 columnas
4 Numericas
1 Categorica

**6. Dataframe 'PROCEDURES_ICD.csv'**
506 Filas
5 columnas
5 numericas

**7. Dataframe 'PATIENTS.csv'**
100 Filas
8 Columnas
2 numericas
6 categoricas

Reporte:

1 . Los valores de de ID empiezan con 1 o con 3 lo que puede suponer una diferenciacion entre los registros
2 . Los valores de de ID empiezan con 1 o con 4 lo que puede suponer una diferenciacion entre pacientes
3 . Las mujeres sobrepasan a los hombres por 10 puntos porcentuales en el dataset
8 . Todos los pacientes están muertos.

Las Variables que necesitan transformaciones:
1. Pasar las columnas ["religion", "ethnicity", "language", "marital_status", "Insurance"] de la tabla ADMISSIONS a la tabla PATIENTS
2. Sacar la edad del paciente

**8. Dataframe D_ICD_DIAGNOSES.csv**
3882 Filas
4 columnas
1 numericas
3 categorica

Reporte
Esta tabla corresponde a Diccionario internacional. Clasificación de Enfermedades-Diagnósticos

la tabla cuenta con 14567 registros y 4 dimensiones
No presenta valores faltantes
-se sugiere agregar una columna que simplifique el diagnóstico.

**9 Dataframe D_ICD PROCEDURES**
1467 Filas
4 columnas
4 numericas


Reporte:

La tabla no contiene ningun valor nulo y todos los valores son distintos porque se tratan de descripciones acerca de los procedimientos que se le hicieron al paciente.

La columna 'short_title' contiene abreviaciones de los procedimientos que no se cumplen en todos los casos.
Las variables que necesitan Transformación:
La clumna "short title' evaluar si normalizar o eliminar.

**10.Dataframe D_CPT.csv**
134 filas
9 Columnas
3 numericas
6 categoricas

Reporte:
El dataset es un CPT que es un catalogo de los servicios medicos que brinda la estancia.

2 . los servicios se dividen en 3 grupos, la mayoria se ubican en el grupo 1

4 . Los servicios estan distribuidos de una forma relativamente uniforme pero es Medicine la que destaca del resto.

7 . tiene solo 11 registros por lo que se puede considerar eliminar

Transformaciones:

Decidir si eliminar 'codesuffix' porque ya de por si 'sectionrange' tiene el sufijo.

**11.Dataframe ICUSTAYS.csv**
136 filas
12 columnas
5 numericas
5.Categoricas
2 Texto
1. Se puede calcular el tiempo que duro un paciente dentro de la UCI con las columnas 'intime' y 'outtime'
2. La tabla no contiene valores nulos


**12.Dataframe ADMISIONS.csv**
129 filas
19 columnas
3 numericas
10 categoricas
3 texto
En la columna 'deathtime' se encuentra un valor como NaT el cual toca remplazarlo
En la columna 'hospital_expire_flag' se encuentra en valores booleanos, la satisfaccion del paciente


**13.Dataframe D_LABINTEMS.csv**
753 filas
6 columnas
2 numericas
2 categoricas
2 texto
Se necesita pasar las columnas de tipo 'STR' a minuscula ya que hay mismos valores escritos en mayuscula.

**14.Dataframe LABEVENTS.csv**
76064 Filas
9 Columnas
4 Categoricas
5 Nunmericas

Reporte:
Esta tabla corresponde a eventos relacionados con pruebas de laboratorio
- la tabla cuenta con 76074 registros y 9 dimensiones
- corresponden a los valores de laboratorio de 100 pacientes (subject_id), con 129 admisiones (hadm_id), es decir que hay 29 son readmisiones
- la dimensión flag, contiene la mayor cantidad de 'faltantes', pero estos corresponden a valores normales. Por lo tanto hay que corregir

**15.Dataframe NOTEEVENTS.csv**
11 columnas
Reporte:
Esta tabla no tiene registros, por ende no se puede sacar conclusiones de esta tabla.
**16.TRANFERS.csv**
524 filas
13 columnas
7 numericas
6 categoricas
Reporte: 
Esta tabla corresponde a la ubicación de los pacientes durante su estancia hospitalaria
- la tabla cuenta con 524 registros y 13 dimensiones
- contamos con el registro de 100 pacientes (subject_id distintos), que ingresaron 167 veces a UCI (icustay_id) en distintos tiempos.
-La columna 'icustay_id', 'prev_careunit' y 'curr_careunit' cuentan con la misma cantidad de faltantes, esto es debido a que el paciente todavía no ingreso a UCI .


**17.Dataframe PRESCRIPTIONS.csv**
**18.Dataframe  D_ITEMS.csv**
12467 filas
10 columnas
2 numericas
5 categoricas
3 texto
Reporte
La columna 'conceptid' no se usa, por ende, se puede eliminar de la tabla
Hay valores confusos en la columna 'unitname' como lo son: '?C' y '?F'.
Los cuales se puede cambiar por: 'centigrade' y 'fahrenheit'.

**19.Dataframe CAREGIVERS.csv**
7567 Filas
4 columnas
2 numericas
1 categorica
1 texto

*Reporte:*
3 . cada valor de label está escrito de una forma distinta por lo que no se produce una grafica interesante,

4 . Label y Description están completamente relacionadas, los RO y los Res sobrepasan al resto.

**20.Dataframe INPUTEVENTS_CV.csv**
34799 filas
22 columnas
12 numericas
8 categoricas
2 texto
*Reporte:*
El dataset trata de las veces en que se e suministró un medicamente a un paciente, con sus dosis en las unidades de medida correspondientes. Los datos nulos son muy frecuentes lo que puede suponer un problema.

4 . El icustay_id con mas suministros fue el 249805 con 22% del total que destaca del resto

8 . La mayoria de los medicamentos se suministran en ml (71%) o mg (18%)

10 . las unidades de medida no tienen un / de separacion

19 . Los tratamientos que mas se repiten son los intravenosos (62%)

21 . tiene solo un valor ("ml/hr")

22 . Esta columna solo tiene 6 registros.
Transformaciones:

* Decidir si eliminar las columnas stopped, newbottle que tienen mayoria nulos

* Decidir si eliminar la columna originalrateuom que tiene solo un valor

* Eliminar originalsite

**21.Dataframe INPUTEVENTS_MV.csv**
13224 filas
31 columnas
13 categoricas
12 numericas
4 texto
Reporte
Transformar valore NaN de las columnas 
'comments_editedby' (90% NaN)
'comments_canceledby' (96% Nan)
Comments_date (87% NaN)
Cambiar formato fecha 'starttime,endtime'





**22.Dataframe DATETIMEEVENTS.csv**
15551 Filas
14 Columnas
4 Categoricas
6 Numericas
4 Texto
Transformaciones
1. Eliminar 'resultstatus', es una columna 100% vacia
2. La columna'stopped' tiene valores vacios (70% NaN)
3. Cambio formato de fecha:'charttime', 'storetime','value'



**23.Dataframe CHARTEVENTS.csv**

**24.Dataframe OUTPUTEVENTS.csv**
11320 Filas
13 Columnas
1 Categorica
7 Numericas
5 Texto
Transformaciones:
Cambio formato de Fecha 'chartime','storettime'.
Eliminar columnas
'stopped'(100% NaN), newbottle(100% NaN), 'iserror'(100%)


**25.Dataframe PROCEDUREEVENTS_MV**
753 Filas
25 Columnas
11 Categoricas
9 Numericas
5 Texto
Transformaciones 
Cambio de formato de Fecha 'starttime', 'endtime', storetime, comments_date
Valores nulos: 'location' (84% NaN), 'locationcategory'(84% NaN)
Eliminar las columnas (>95% NaN) 'secondaryordercategoryname'
'comments_editedby'
'commnets_canceldby'
'comments_date'
**26.Dataframe MICROBIOLOGYEVENTS**
2003 Filas
16 Columnas
7 Categoricas
7 Numericas
2 Texto
Transformaciones:
Formato cambio Fecha:
'chardate', charttime'














