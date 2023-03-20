import pandas as pd
import numpy as np

#Funcion para cambiar a tipo fecha
def cambiar_a_fecha(df, columnas):
    for i in columnas:
        df[i] = pd.to_datetime(df[i])
        
#Funcion para cambiar a minusculas
def cambiar_a_minuscula(df, columnas):
    for i in columnas:
        df[i] = df[i].str.lower()


ADMISSIONS = pd.read_csv('Datasets/Normal/ADMISSIONS.csv')
CALLOUT = pd.read_csv('Datasets/Normal/CALLOUT.csv')
CAREGIVERS = pd.read_csv('Datasets/Normal/CAREGIVERS.csv')
CHARTEVENTS = pd.read_csv('Datasets/Normal/CHARTEVENTS.csv')
CPTEVENTS = pd.read_csv('Datasets/Normal/CPTEVENTS.csv')
D_CPT = pd.read_csv('Datasets/Normal/D_CPT.csv')
D_ICD_DIAGNOSES = pd.read_csv('Datasets/Normal/D_ICD_DIAGNOSES.csv')
D_ICD_PROCEDURES = pd.read_csv('Datasets/Normal/D_ICD_PROCEDURES.csv')
D_ITEMS = pd.read_csv('Datasets/Normal/D_ITEMS.csv')
D_LABITEMS = pd.read_csv('Datasets/Normal/D_LABITEMS.csv')
DATETIMEEVENTS = pd.read_csv('Datasets/Normal/DATETIMEEVENTS.csv')
DIAGNOSES_ICD = pd.read_csv('Datasets/Normal/DIAGNOSES_ICD.csv')
DRGCODES = pd.read_csv('Datasets/Normal/DRGCODES.csv')
ICUSTAYS = pd.read_csv('Datasets/Normal/ICUSTAYS.csv')
INPUTEVENTS_CV = pd.read_csv('Datasets/Normal/INPUTEVENTS_CV.csv')
INPUTEVENTS_MV = pd.read_csv('Datasets/Normal/INPUTEVENTS_MV.csv')
LABEVENTS = pd.read_csv('Datasets/Normal/LABEVENTS.csv')
MICROBIOLOGYEVENTS = pd.read_csv('Datasets/Normal/MICROBIOLOGYEVENTS.csv')
OUTPUTEVENTS = pd.read_csv('Datasets/Normal/OUTPUTEVENTS.csv')
PATIENTS = pd.read_csv('Datasets/Normal/PATIENTS.csv')
PRESCRIPTIONS = pd.read_csv('Datasets/Normal/PRESCRIPTIONS.csv')
PROCEDUREEVENTS_MV = pd.read_csv('Datasets/Normal/PROCEDUREEVENTS_MV.csv')
PROCEDURES_ICD = pd.read_csv('Datasets/Normal/PROCEDURES_ICD.csv')
SERVICES = pd.read_csv('Datasets/Normal/SERVICES.csv')
TRANSFERS = pd.read_csv('Datasets/Normal/TRANSFERS.csv')


# ADMISSIONS

# Se hace el cambio de tipo de dato a fecha
cambiar_a_fecha(ADMISSIONS, ['admittime', 'dischtime', 'deathtime', 'edregtime', 'edouttime']) 


# CALLOUT
CALLOUT.fillna(0, inplace = True)

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(CALLOUT, ["createtime", "updatetime", "acknowledgetime", "outcometime", "firstreservationtime", "currentreservationtime"])


#CAREGIVERS
#Evaluar necesidad de homogeneizer 'label'


# CHARTEVENTS
# Convertimos los datos a un formato apropiado
cambiar_a_fecha(CHARTEVENTS, ["charttime", "storetime"])

# columna 'value' tiene datos que no corresponder. Se elimina y se usan datos de 'valueuom'  !!!!!
CHARTEVENTS.drop(['value'], axis=1, inplace=True)


# CPTEVENTS

CPTEVENTS.fillna(0, inplace = True)


# D_CPT
# Eliminamos columna codesuffix que contiene solo 11 datos
D_CPT.drop(['codesuffix'], axis=1, inplace=True)


# D_ICD_DIAGNOSES

#Se agrega columna con supercategorías, para simplificar la visualización del diagnóstico
#ICD-9 codes supercategories: https://en.wikipedia.org/wiki/List_of_ICD-9_codes

# Filtro los códigos E y V de los códigos, ya que el procesamiento se realiza en los primeros 3 valores
D_ICD_DIAGNOSES['recode'] = D_ICD_DIAGNOSES['icd9_code']
D_ICD_DIAGNOSES['recode'] = D_ICD_DIAGNOSES['recode'][~D_ICD_DIAGNOSES['recode'].str.contains("[a-zA-Z]").fillna(False)]
D_ICD_DIAGNOSES['recode'].fillna(value='999', inplace=True)

# Se tienen en cuenta solo los primeros 3 enteros del código ICD9
D_ICD_DIAGNOSES['recode'] = D_ICD_DIAGNOSES['recode'].str.slice(start=0, stop=3, step=1)
D_ICD_DIAGNOSES['recode'] = D_ICD_DIAGNOSES['recode'].astype(int)

# ICD-9 Rangos de Categorías principales
icd9_ranges = [(1, 140), (140, 240), (240, 280), (280, 290), (290, 320), (320, 390), 
               (390, 460), (460, 520), (520, 580), (580, 630), (630, 680), (680, 710),
               (710, 740), (740, 760), (760, 780), (780, 800), (800, 1000), (1000, 2000)]

# Nombres asociados a las categorías
diag_dict = {0: 'infectious', 1: 'neoplasms', 2: 'endocrine', 3: 'blood',
             4: 'mental', 5: 'nervous', 6: 'circulatory', 7: 'respiratory',
             8: 'digestive', 9: 'genitourinary', 10: 'pregnancy', 11: 'skin', 
             12: 'muscular', 13: 'congenital', 14: 'prenatal', 15: 'misc',
             16: 'injury', 17: 'misc'}

# Re-codificación en términos de enteros
for num, cat_range in enumerate(icd9_ranges):
    D_ICD_DIAGNOSES['recode'] = np.where(D_ICD_DIAGNOSES['recode'].between(cat_range[0],cat_range[1]), num, D_ICD_DIAGNOSES['recode'])
    
# Convert integer to category name using diag_dict
D_ICD_DIAGNOSES['super_category'] = D_ICD_DIAGNOSES['recode'].replace(diag_dict)


# D_ITEMS

# Se pasa las columnas a minusculas para que no hayan valores repetidos escritos de distinta forma
cambiar_a_minuscula(D_ITEMS, ['unitname']) 

# Se realiza un for para cambiar un tipo de dato y hacerlo mas legible
for i in range(0, len(D_ITEMS)):
    if D_ITEMS['unitname'].loc[i] == '?c':
        D_ITEMS['unitname'].loc[i] = 'centigrade'
    elif D_ITEMS['unitname'].loc[i] == '?f':
        D_ITEMS['unitname'].loc[i] = 'fahrenheit'

# Se elimina una columna de la tabla ya que no tiene ningun uso ni ningn registro
D_ITEMS.drop(['conceptid'], axis = 1, inplace = True)


# D_LABITEM

# Se pasa las columnas a minusculas para que no hayan valores repetidos escritos de distinta forma
cambiar_a_minuscula(D_LABITEMS, ["label", "fluid", "category"]) 

# Se realiza un for para cambiar un dato repetido escrito de distinta forma 
for i in range(0, len(D_LABITEMS)):
    if D_LABITEMS['fluid'].loc[i] == 'csf':
        D_LABITEMS['fluid'].loc[i] = 'cerebrospinal fluid (csf)'


# DATETIMEEVENTS

# Eliminamos columnas con pocos datos
DATETIMEEVENTS.drop(['resultstatus'], axis=1, inplace=True)

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(DATETIMEEVENTS, ["charttime", "storetime"])


# DRGCODES
DRGCODES.fillna(0, inplace = True)
        

# ICUSTAYS

# Se hace el cambio de tipo de dato a fecha 
cambiar_a_fecha(ICUSTAYS, ["intime", "outtime"])


# INPUTEVENTS_CV

# Eliminamos columnas con pocos datos
INPUTEVENTS_CV.drop(['originalsite'], axis=1, inplace=True)
INPUTEVENTS_CV.drop(['stopped'], axis=1, inplace=True)
INPUTEVENTS_CV.drop(['newbottle'], axis=1, inplace=True)

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(INPUTEVENTS_CV, ["charttime"])


# INPUTEVENTS_MV

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(INPUTEVENTS_MV, ["starttime", "storetime"])


# LABEVENTS

# Flag, marcador que indica si el valor de prueba de laboratorio es anormal (NULL= normal), marcamos esta distinción con una variable booleana
LABEVENTS['flag1'] = LABEVENTS['flag'].notnull().map({True:1, False:0})

# Elimino columna y renombro
LABEVENTS.drop(['flag'], axis=1, inplace=True)
LABEVENTS.rename(columns={'flag1': 'flag'}, inplace=True)

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(LABEVENTS, ["charttime"])


# MICRIOBIOLOGYEVENTS

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(MICROBIOLOGYEVENTS, ["charttime", "chartdate"])


# PATIENTS

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(PATIENTS, ["dob", "dod", "dod_hosp", "dod_ssn"])

# obtener la marca de tiempo en segundos
PATIENTS['dob_hr'] = PATIENTS['dob'].apply(lambda x: x.timestamp()) / 3600
PATIENTS['dod_hr'] = PATIENTS['dod'].apply(lambda x: x.timestamp()) / 3600

# Sacar columna edad
PATIENTS['age'] = round((PATIENTS['dod_hr'] - PATIENTS["dob_hr"]) / (365 * 24))

#Eliminamos columnas dod_hr y dob_hr??


# PRESCRIPTIONS

# Se hace el cambio de tipo de dato a fecha
cambiar_a_fecha(PRESCRIPTIONS, ['startdate', 'enddate']) 


# PROCEDUREEVENTS_MV

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(PROCEDUREEVENTS_MV, ["starttime", "endtime", "storetime"])


# PROCEDURES_ICD

PROCEDURES_ICD.fillna(0, inplace = True)


# SERVICES
SERVICES.fillna(0, inplace = True)
cambiar_a_fecha(SERVICES, ["transfertime"])


# TRANSFERS

# Convertimos los datos a un formato apropiado
cambiar_a_fecha(TRANSFERS, ["intime", "outtime"])


# # Guardo el dataset limpio para el siguiente proceso  ??????
ADMISSIONS.to_csv('Datasets/Transformations/ADMISSIONS_C.csv', index=False)
CALLOUT.to_csv('Datasets/Transformations/CALLOUT_C.csv', index=False)
CAREGIVERS.to_csv('Datasets/Transformations/CAREGIVERS_C.csv', index=False)
CHARTEVENTS.to_csv('Datasets/Transformations/CHARTEVENTS_C.csv', index=False)
CPTEVENTS.to_csv('Datasets/Transformations/CPTEVENTS_C.csv', index=False)
D_CPT.to_csv('Datasets/Transformations/D_CPT_C.csv', index=False)
D_ICD_DIAGNOSES.to_csv('Datasets/Transformations/D_ICD_DIAGNOSES.csv', index = False)
D_ICD_PROCEDURES.to_csv('Datasets/Transformations/D_ICD_PROCEDURES_C.csv', index=False)
D_ITEMS.to_csv('Datasets/Transformations/D_ITEMS_C.csv', index=False)
D_LABITEMS.to_csv('Datasets/Transformations/D_LABITEMS_C.csv', index=False)
DATETIMEEVENTS.to_csv('Datasets/Transformations/DATETIMEEVENTS_C.csv', index=False)
DIAGNOSES_ICD.to_csv('Datasets/Transformations/DIAGNOSES_ICD.csv', index = False)
DRGCODES.to_csv('Datasets/Transformations/DRGCODES_C.csv', index=False)
ICUSTAYS.to_csv('Datasets/Transformations/ICUSTAYS_C.csv', index=False)
INPUTEVENTS_CV.to_csv('Datasets/Transformations/INPUTEVENTS_CV_C.csv', index=False)
INPUTEVENTS_MV.to_csv('Datasets/Transformations/INPUTEVENTS_MV_C.csv', index=False)
LABEVENTS.to_csv('Datasets/Transformations/LABEVENTS_C.csv', index=False)
MICROBIOLOGYEVENTS.to_csv('Datasets/Transformations/MICROBIOLOGYEVENTS.csv', index=False)
OUTPUTEVENTS .to_csv('Datasets/Transformations/OUTPUTEVENTS _C.csv', index=False)
PATIENTS.to_csv('Datasets/Transformations/PATIENTS_C.csv', index=False)
PRESCRIPTIONS.to_csv('Datasets/Transformations/PRESCRIPTIONS.csv', index = False)
PROCEDUREEVENTS_MV.to_csv('Datasets/Transformations/PROCEDUREEVENTS_MV_C.csv', index=False)
PROCEDURES_ICD.to_csv('Datasets/Transformations/CHARTEVENTS_C.csv', index=False)
SERVICES.to_csv('Datasets/Transformations/SERVICES_C.csv', index=False)
TRANSFERS.to_csv('Datasets/Transformations/TRANSFERS_C.csv', index=False)