import pandas as pd
import numpy as np
import LoadDB as db


#Funcion para cambiar a tipo fecha
def cambiar_a_fecha(df, columnas):
    for i in columnas:
        df[i] = pd.to_datetime(df[i])
        df[i].fillna('1999-01-01', inplace=True)    # Cambio valores faltantes de fechas por '1999-01-01'

        
#Funcion para cambiar a minusculas
def cambiar_a_minuscula(df, columnas):
    for i in columnas:
        df[i] = df[i].str.lower()


# 1) ETL tabla ADMISSIONS

def etl_admissions(df):
    # Se crea una nueva columna boolena que muestra los pacientes fallecidos con 1
    df['died_at_the_hospital'] = df['deathtime'].notnull().map({True:1, False:0})
    # Se hace el cambio de tipo de dato a fecha
    cambiar_a_fecha(df, ['admittime', 'dischtime', 'deathtime', 'edregtime', 'edouttime']) 
    df.fillna(0, inplace = True)    # Se Remplazan los Valores vacios o NaN por 0

    return df


# 2) ETL tabla CALLOUT

def etl_callout(df):
    # Convertimos los datos a un formato apropiado
    cambiar_a_fecha(df, ["createtime", "updatetime", "acknowledgetime", "outcometime", "firstreservationtime", "currentreservationtime"])
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 3) ETL tabla CAREGIVERS

def etl_caregivers(df):
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 4) ETL tabla CHARTEVENTS

def etl_chartevents(df):
    # Convertimos los datos a un formato apropiado
    cambiar_a_fecha(df, ["charttime", "storetime"])

    # Se realiza un for para cambiar un tipo de dato y hacerlo mas legible
    for i in range(0, len(df)):
        if df['valueuom'].loc[i] == '?C':
            df['valueuom'].loc[i] = 'centigrade'
        elif df['valueuom'].loc[i] == 'Deg. C':
            df['valueuom'].loc[i] = 'centigrade'
        elif df['valueuom'].loc[i] == '?F':
            df['valueuom'].loc[i] = 'fahrenheit'
        elif df['valueuom'].loc[i] == 'Deg. F':
            df['valueuom'].loc[i] = 'fahrenheit'

    # Columna 'value' tiene datos que no corresponder. Se elimina y se usan datos de 'valueuom' 
    df.drop(['value'], axis=1, inplace=True)
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 5) ETL tabla CPTEVENTS

def etl_cptevents(df):
    cambiar_a_fecha(df, ['chartdate'])  # Cambiamos los datos a un formato apropiado
    df.drop(['cpt_suffix'], axis=1, inplace=True)   # Se elimina columna 'cpt_suffix' sin valores
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 6) ETL tabla D_CPT

def etl_d_cpt(df):
    df.drop(['codesuffix'], axis=1, inplace=True)   # Eliminamos columna codesuffix que contiene solo 11 datos
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 7) ETL tabla D_ICD_DIAGNOSES

'''
Se agrega columna con supercategorías, para simplificar la visualización del diagnóstico
ICD-9 codes supercategories: https://en.wikipedia.org/wiki/List_of_ICD-9_codes
'''

def etl_d_icd_diagnoses(df):
    # Filtro los códigos E y V de los códigos, ya que el procesamiento se realiza en los primeros 3 valores
    df['recode'] = df['icd9_code']
    df['recode'] = df['recode'][~df['recode'].str.contains("[a-zA-Z]").fillna(False)]
    df['recode'].fillna(value='999', inplace=True)

    # Se tienen en cuenta solo los primeros 3 enteros del código ICD9
    df['recode'] = df['recode'].str.slice(start=0, stop=3, step=1)
    df['recode'] = df['recode'].astype(int)

    #ICD-9 Rangos de Categorías principales
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
        df['recode'] = np.where(df['recode'].between(cat_range[0],cat_range[1]), num, df['recode'])  

    # Convertir entero a un nombre de categoria usando diag_dict
    df['super_category'] = df['recode'].replace(diag_dict)

    df.drop(['recode'], axis=1, inplace=True)   #eliminamos columna auxiliar
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 8) ETL tabla D_ICD_PROCEDURES

def etl_d_icd_procedures(df):
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 9) ETL tabla D_ITEMS

def etl_d_items(df):
    # Se pasa las columnas a minusculas para que no hayan valores repetidos escritos de distinta forma
    cambiar_a_minuscula(df, ['unitname']) 

    # Se realiza un for para cambiar un tipo de dato y hacerlo mas legible
    for i in range(0, len(df)):
        if df['unitname'].loc[i] == '?c':
            df['unitname'].loc[i] = 'centigrade'
        elif df['unitname'].loc[i] == '?f':
            df['unitname'].loc[i] = 'fahrenheit'
            
    df.drop(['conceptid'], axis = 1, inplace = True)    # Se elimina una columna de la tabla ya que no tiene ningun uso ni ningn registro
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 10) ETL tabla D_LABITEM

def etl_d_labitem(df):
    # Se pasa las columnas a minusculas para que no hayan valores repetidos escritos de distinta forma
    cambiar_a_minuscula(df, ["label", "fluid", "category"])

    # Se realiza un for para cambiar un dato repetido escrito de distinta forma 
    for i in range(0, len(df)):
        if df['fluid'].loc[i] == 'csf':
            df['fluid'].loc[i] = 'cerebrospinal fluid (csf)'

    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 11) ETL tabla DATETIMEEVENTS

def etl_datetimeevents(df):
    df.drop(['resultstatus'], axis=1, inplace=True) # Eliminamos columnas con pocos datos
    cambiar_a_fecha(df, ["charttime", "storetime", "value"])    # Convertimos los datos a un formato apropiado
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 12) ETL tabla DIAGNOSES_ICD

def etl_diagnoses_icd(df):
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 13) ETL tabla DRGCODES

def etl_drgcodes(df):
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 14) ETL tabla ICUSTAYS

def etl_icustays(df):
    cambiar_a_fecha(df, ["intime", "outtime"]) # Se hace el cambio de tipo de dato a fecha
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 15) ETL tabla INPUTEVENTS_CV

def etl_inputevents_cv(df):
    # Eliminamos columnas con pocos datos
    df.drop(['originalsite', 'stopped', 'newbottle', 'originalrateuom', 'originalrate', 'rate', 'rateuom'], axis=1, inplace=True)

    cambiar_a_fecha(df, ["charttime", "storetime"])  # Convertimos los datos a un formato apropiado
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 16) ETL tabla INPUTEVENTS_MV

def etl_inputevents_mv(df):
    df.drop(['comments_canceledby', 'comments_date'], axis=1, inplace=True)    # Eliminamos columnas con pocos datos
    cambiar_a_fecha(df, ["starttime", "endtime", "storetime"])   # Convertimos los datos a un formato apropiado
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 17) ETL tabla LABEVENTS

def etl_labevents(df): 
    # Flag, marcador que indica si el valor de prueba de laboratorio es anormal (NULL= normal), marcamos esta distinción con una variable booleana
    df['flag1'] = df['flag'].notnull().map({True:1, False:0})
    
    # Elimino columna y renombro
    df.drop(['flag'], axis=1, inplace=True)
    df.rename(columns={'flag1': 'flag'}, inplace=True)

    # Convertimos los datos a un formato apropiado
    cambiar_a_fecha(df, ["charttime"])

    df.drop(['value'], axis=1, inplace=True)    # Eliminamos columna 'value' que contiene datos que no corresponden a la dimensión
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 18) ETL tabla MICRIOBIOLOGYEVENTS

def etl_micriobiologyevents(df):
    cambiar_a_fecha(df, ["charttime", "chartdate"]) # Convertimos los datos a un formato apropiado
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 19) ETL tabla OUTPUTEVENTS 

def etl_outputevents(df):
    cambiar_a_fecha(df, ['charttime', 'storetime']) # Convertimos los datos a un formato apropiado
    df.drop(['stopped', 'newbottle', 'iserror'], axis=1, inplace=True)  # Se eliminan columnas innecesarias
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 20) ETL tabla PATIENTS

def etl_patients(df):
    # Convertimos los datos a un formato apropiado
    cambiar_a_fecha(df, ["dob", "dod", "dod_hosp", "dod_ssn"])

    # obtener la marca de tiempo en segundos
    df['dob_hr'] = df['dob'].apply(lambda x: x.timestamp()) / 3600
    df['dod_hr'] = df['dod'].apply(lambda x: x.timestamp()) / 3600

    # Se agrega columna edad
    df['age'] = round((df['dod_hr'] - df["dob_hr"]) / (365 * 24))

    df.drop(['dod_hr', 'dob_hr'], axis=1, inplace=True) # Eliminamos columnas auxiliares
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 21) ETL tabla PRESCRIPTIONS

def etl_prescriptions(df):
    cambiar_a_fecha(df, ['startdate', 'enddate'])   # Se hace el cambio de tipo de dato a fecha
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df 


# 22) ETL tabla PROCEDUREEVENTS_MV

def etl_procedureevents_mv(df):
    # Convertimos los datos a un formato apropiado
    cambiar_a_fecha(df, ["starttime", "endtime", "storetime"])

    # Eliminamos columnas con pocos datos
    df.drop(['secondaryordercategoryname', 'comments_editedby', 'comments_canceledby', 'comments_date', 'location', 'locationcategory'], axis=1, inplace=True)

    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 23) ETL tabla PROCEDURES_ICD

def etl_procedures_icd(df):
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 24) ETL tabla SERVICES

def etl_services(df):
    cambiar_a_fecha(df, ["transfertime"])
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df


# 25) ETL tabla TRANSFERS

def etl_transfers(df):
    cambiar_a_fecha(df, ["intime", "outtime"])  # Convertimos los datos a un formato apropiado
    df.fillna(0, inplace = True)    # Se remplaza los valores vacios o Nan por 0

    return df

# 26) ETL modelo de estancia en UCI

def etl_model_train_stay():

    # ------------------------------------------------------------ ADMISSIONS


    # Se cargan los datos de la tabla 'ADMISSIONS' de la base de datos
    dfAdmissions = pd.DataFrame(db.selectTableAdmissions())

    # Se cambia el nombre de las columnas
    dfAdmissions.columns = ['row_id','subject_id','hadm_id','admittime','dischtime','deathtime',
              'admission_type','admission_location','discharge_location','insurance',
              'language','religion','marital_status','ethnicity','edregtime',
              'edouttime','diagnosis','hospital_expire_flag','has_chartevents_data',
              'died_at_the_hospital']
    
    dfAdmissions = dfAdmissions[['subject_id','hadm_id', 'admittime', 'dischtime', 'deathtime', 
                                 'admission_type', 'insurance', 'ethnicity', 'died_at_the_hospital']]

    # # Cambiamos el tipo de fecha de las columnas
    # dfAdmissions.admittime = pd.to_datetime(dfAdmissions.admittime)
    # dfAdmissions.dischtime = pd.to_datetime(dfAdmissions.dischtime)
    # dfAdmissions.deathtime = pd.to_datetime(dfAdmissions.deathtime)

    # Se unen algunos registros para tener mas pocos
    dfAdmissions['ethnicity'].replace(regex=r'^ASIAN\D*', value='ASIAN', inplace=True)
    dfAdmissions['ethnicity'].replace(regex=r'^WHITE\D*', value='WHITE', inplace=True)
    dfAdmissions['ethnicity'].replace(regex=r'^HISPANIC\D*', value='HISPANIC/LATINO', inplace=True)
    dfAdmissions['ethnicity'].replace(regex=r'^BLACK\D*', value='BLACK/AFRICAN AMERICAN', inplace=True)
    dfAdmissions['ethnicity'].replace(['UNABLE TO OBTAIN', 'OTHER', 'PATIENT DECLINED TO ANSWER', 
                            'AMERICAN INDIAN/ALASKA NATIVE FEDERALLY RECOGNIZED TRIBE', 'UNKNOWN/NOT SPECIFIED'], value='OTHER/UNKNOWN', inplace=True)

    # Se tendra en cuenta solo las 5 primeras grades categorias, las demas, se añadiran a 'OTHER'
    dfAdmissions['ethnicity'].loc[~dfAdmissions['ethnicity'].isin(dfAdmissions['ethnicity'].value_counts().nlargest(5).index.tolist())] = 'OTHER/UNKNOWN'  

    # Se unen los registros con mismo significado pero que aparecen escritos de distinta forma para el caso de 'EMERGENCY'
    dfAdmissions['admission_type'].replace(to_replace='URGENT', value='EMERGENCY', inplace=True)  


    # ------------------------------------------------------------ PATIENTS

    # Se cargan los datos de la tabla 'PATIENTS' de la base de datos
    dfPatients = pd.DataFrame(db.selectTablePatients())

    # Se cambia el nombre de las columnas
    dfPatients.columns = ['row_id','subject_id','gender','dob','dod','dod_hosp','dod_ssn','expire_flag','age']

    dfPatients = dfPatients[['subject_id', 'gender', 'age', 'dod', 'dob']]

    # # Cambiamos el tipo de dato a fecha 
    # dfPatients.dod = pd.to_datetime(dfPatients.dod)
    # dfPatients.dob = pd.to_datetime(dfPatients.dob)


    # ------------------------------------------------------------ DIAGNOSES_ICD


    # Se cargan los datos de la tabla 'DIAGNOSES_ICD' de la base de datos
    dfDiagnoses = pd.DataFrame(db.selectTableDiagnoses_icd())

    # Se cambia el nombre de las columnas 
    dfDiagnoses.columns = ['row_id','subject_id','hadm_id','seq_num','icd9_code']

    # Se filtra por letras y se modifica para que no aparezcan
    dfDiagnoses['recode'] = dfDiagnoses['icd9_code']
    dfDiagnoses['recode'] = dfDiagnoses['recode'][~dfDiagnoses['recode'].str.contains("[a-zA-Z]").fillna(False)]
    dfDiagnoses['recode'].fillna(value='999', inplace=True)

    # Se toma unicamente los 3 primeros valores numericos 
    dfDiagnoses['recode'] = dfDiagnoses['recode'].str.slice(start=0, stop=3, step=1)
    dfDiagnoses['recode'] = dfDiagnoses['recode'].astype(int)

    # Se crea el rango de categorias para la columna 'recode'
    icd9_ranges = [(1, 140), (140, 240), (240, 280), (280, 290), (290, 320), (320, 390), 
                (390, 460), (460, 520), (520, 580), (580, 630), (630, 680), (680, 710),
                (710, 740), (740, 760), (760, 780), (780, 800), (800, 1000), (1000, 2000)]

    # Se asocian los nombres segun el rango de codigo
    diag_dict = {0: 'infectious', 1: 'neoplasms', 2: 'endocrine', 3: 'blood',
                4: 'mental', 5: 'nervous', 6: 'circulatory', 7: 'respiratory',
                8: 'digestive', 9: 'genitourinary', 10: 'pregnancy', 11: 'skin', 
                12: 'muscular', 13: 'congenital', 14: 'prenatal', 15: 'misc',
                16: 'injury', 17: 'misc'}

    # Se tranforma la columna 'recode' asociando las enfermedades del diccionario que creamos
    for num, cat_range in enumerate(icd9_ranges):
        dfDiagnoses['recode'] = np.where(dfDiagnoses['recode'].between(cat_range[0],cat_range[1]), num, dfDiagnoses['recode'])

    # Se crea la columna 'super_category' para almacenar el nombre de las enfermedades
    dfDiagnoses['super_category'] = dfDiagnoses['recode'].replace(diag_dict)

    # Se crea una matriz la cual señala los diagnosticos de cada admision
    hadm_list = dfDiagnoses.groupby('hadm_id')['super_category'].apply(list).reset_index()

    # Se cre una matriz que contiene la cantidad de veces que hubo una enfermedad por cada admision
    hadm_item = pd.get_dummies(hadm_list['super_category'].apply(pd.Series).stack()).sum(level=0)

    # Se agrega el id de admisiones
    hadm_item = hadm_item.join(hadm_list['hadm_id'], how="outer")


    # ------------------------------------------------------------ ICUSTAYS


    # Se cargan los datos de la tabla 'ICUSTAYS' de la base de datos 
    dfIcustays = pd.DataFrame(db.selectTableIcustays())

    # Se cambia el nombre de las columas
    dfIcustays.columns = ['row_id','subject_id','hadm_id','icustay_id','dbsource','first_careunit',
                          'last_careunit','first_wardid','last_wardid','intime','outtime','los']

    # Se agrupan las categorias 
    dfIcustays['category'] = dfIcustays['first_careunit']
    icu_list = dfIcustays.groupby('hadm_id')['category'].apply(list).reset_index()

    # Se crea una matris para las categorias que se crearon
    icu_item = pd.get_dummies(icu_list['category'].apply(pd.Series).stack()).sum(level=0)
    icu_item[icu_item >= 1] = 1
    icu_item = icu_item.join(icu_list['hadm_id'], how="outer")


    # ------------------------------------------------------------ UNIFICACION 1


    # Unimos las tablas de ADMISSIONS y PATIENTS
    admits_patients = pd.merge(dfAdmissions, dfPatients, how='inner', on='subject_id')

    # Se unen las tablas 'admits_patients' y 'hadm_item' anteriormente creadas para tener el DF que vamos a usar para el modelo
    admits_patients_diag = pd.merge(admits_patients, hadm_item, how='inner', on='hadm_id')



    # ------------------------------------------------------------ admits_patients_diag


    # Creamos la columna 'los' la cual pondremos el tiempo que duro un paciente en uci
    admits_patients_diag['los'] = round((admits_patients_diag['dischtime'] - admits_patients_diag['admittime']).dt.total_seconds()/86400)

    # Eliminamos filas con registros de 'los' negativos
    admits_patients_diag = admits_patients_diag[admits_patients_diag['los'] > 0]

    # Se cre un rango de edades
    age_ranges = [(0, 13), (14, 36), (37, 56), (57, 400)]

    # Se remplaza los valores de edad segun el rango
    for num, cat_range in enumerate(age_ranges):
        admits_patients_diag['age'] = np.where(admits_patients_diag['age'].between(cat_range[0],cat_range[1]), num, admits_patients_diag['age'])

    # Se cambia los valores de edad por la categoria a la que pertenecen 
    age_dict = {0: 'NEWBORN', 1: 'YOUNG_ADULT', 2: 'MIDDLE_ADULT', 3: 'SENIOR'}
    admits_patients_diag['age'] = admits_patients_diag['age'].replace(age_dict)


    # ------------------------------------------------------------ UNIFICACION 2


    # Se unifica los datos que optuvimos al DF que cargamos inicialmente
    final_df = admits_patients_diag.merge(icu_item, how='outer', on='hadm_id')


    # ------------------------------------------------------------ final_df


    # Se remplazan los valores Nan
    final_df['MICU'].fillna(value=0, inplace=True)
    final_df['CSRU'].fillna(value=0, inplace=True)
    final_df['CCU'].fillna(value=0, inplace=True)
    final_df['SICU'].fillna(value=0, inplace=True)
    final_df['TSICU'].fillna(value=0, inplace=True)

    # Quitamos a las personas fallecidas ya que no son necesarios para el modelo 
    final_df = final_df[final_df['died_at_the_hospital'] == 0]

    # Quitamos valores negativos
    final_df = final_df[final_df['los'] > 0]

    # Quitamos columnas innecesarias
    final_df.drop(columns=['subject_id', 'hadm_id', 'admittime', 'dischtime', 'deathtime',
                    'died_at_the_hospital',  'dod', 'dob'], inplace=True)

    # Convertimos la columna genero en valores booleanos
    final_df['gender'].replace({'M': 0, 'F':1}, inplace=True)

    # Creamos dummies 
    prefix_cols = ['ADM', 'INS', 'ETH', 'AGE']
    dummy_cols = ['admission_type', 'insurance','ethnicity', 'age']
    final_df = pd.get_dummies(final_df, prefix=prefix_cols, columns=dummy_cols)

    final_df.to_csv('dfModels/dfModelSaty.csv', index = False)

    return final_df