import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import streamlit as st
# import ETL_Functions as ef

# ----------------------------------------------- Importando los datos para entrenar el modelo desde la base de datos

# La funcion 'ef.etl_model_train_stay()' se descomenta en el caso que haya una base de datos conectada
# ef.etl_model_train_stay()

final_df = pd.read_csv('dfModels/dfModelSaty.csv')

# ----------------------------------------------- STREAMLIT

test = pd.DataFrame({'gender': [0], 'blood': [0], 'circulatory': [0], 'congenital': [0],
                       'digestive': [0], 'endocrine': [0], 'genitourinary': [0], 'infectious': [0],
                       'injury': [0], 'mental': [0], 'misc': [0], 'muscular': [0], 'neoplasms': [0],
                       'nervous': [0], 'prenatal': [0], 'respiratory': [0], 'skin': [0], 'CCU': [0],
                       'CSRU': [0], 'MICU': [0], 'SICU': [0], 'TSICU': [0], 'ADM_ELECTIVE': [0], 
                       'ADM_EMERGENCY': [0], 'INS_Medicaid': [0], 'INS_Medicare': [0],
                       'INS_Private': [0], 'ETH_ASIAN': [0], 'ETH_BLACK/AFRICAN AMERICAN': [0],
                       'ETH_HISPANIC/LATINO': [0], 'ETH_OTHER/UNKNOWN': [0], 'ETH_WHITE': [0],
                       'AGE_MIDDLE_ADULT': [0], 'AGE_SENIOR': [0], 'AGE_YOUNG_ADULT': [0]})

st.title('MODELO DE ESTANCIA EN UCI')

# Genero

st.header('GENERO')
gender = st.radio('',('Masculino','Femenino'))

if gender == 'Femenino':
    test['gender'] += 1


# Unidad de estancia

st.header('UNIDAD DE ESTANCIA')
stay = st.radio('', ('CCU', 'CSRU', 'MICU', 'SICU', 'TSICU'))

if stay == 'CCU':
    test['CCU'] += 1
elif stay == 'CSRU':
    test['CSRU'] += 1
elif stay == 'MICU':
    test['MICU'] += 1
elif stay == 'SICU':
    test['SICU'] += 1
else:
    test['TSICU'] += 1


# Tipo de admision

st.header('TIPO DE ADMISION')
typeAdmin = st.radio('', ('Electivo', 'Emergencia'))

if typeAdmin == 'Electivo':
    test['ADM_ELECTIVE'] += 1
else:
    test['ADM_EMERGENCY'] += 1


# Seguro

st.header('SEGURO')
insurance = st.radio('', ('Seguro de enfermedad "Medicaid"', 'Seguro medico del estado "Medicare"', 'Privada'))

if insurance == 'Seguro de enfermedad "Medicaid"':
    test['INS_Medicaid'] += 1
elif insurance == 'Seguro medico del estado "Medicare"':
    test['INS_Medicare'] += 1
else:
    test['INS_Private'] += 1


# Etnia

st.header('ETNIA')
ethnicity = st.radio('', ('Asiatico', 'Persona de color/Afro Americano', 'Hispano/Latino', 'Otro/Desconocido', 'Blanco'))

if ethnicity == 'Asiatico':
    test['ETH_ASIAN'] += 1
elif ethnicity == 'Persona de color/Afro Americano':
    test['ETH_BLACK/AFRICAN AMERICAN'] += 1
elif ethnicity == 'Hispano/Latino':
    test['ETH_HISPANIC/LATINO'] += 1
elif ethnicity == 'Otro/Desconocido':
    test['ETH_OTHER/UNKNOWN'] += 1
else:
    test['ETH_WHITE'] += 1


# Edad

st.header('EDAD')
age = st.radio('', ('Jove Adulto (de 14 a 36 años)', 'Adulto (de 37 a 56 años)', 'Señor mayor (de 57 años en adelante)'))

if age == 'Jove Adulto (de 14 a 36 años)':
    test['AGE_YOUNG_ADULT'] += 1
elif age == 'Adulto (de 37 a 56 años)':
    test['AGE_MIDDLE_ADULT'] += 1
else:
    test['AGE_SENIOR'] += 1


# Diagnosticos

st.header('DIAGNOSTICOS') 
st.subheader('Seleccione la cantidad de diagnosticos relacionados a la categoria')

test['blood'] = st.slider('Sangre', 0, 10)
test['circulatory'] = st.slider('Circulacion', 0, 10)
test['congenital'] = st.slider('Congenita', 0, 10)
test['digestive'] = st.slider('Digestion', 0, 10)
test['endocrine'] = st.slider('Endocrina', 0, 10)
test['genitourinary'] = st.slider('genitourinaria', 0, 10)
test['infectious'] = st.slider('Infeccion', 0, 10)
test['injury'] = st.slider('lesion', 0, 10)
test['mental'] = st.slider('Mental', 0, 10)
test['muscular'] = st.slider('Muscular', 0, 10)
test['neoplasms'] = st.slider('Neoplasma', 0, 10)
test['nervous'] = st.slider('Nervios', 0, 10)
test['prenatal'] = st.slider('Prenatal', 0, 10)
test['respiratory'] = st.slider('Respiratorio', 0, 10)
test['skin'] = st.slider('Piel', 0, 10)
test['misc'] = st.slider('Otros', 0, 10)


# ------------------------------------------- MODELO DE PREDICCION


# Usamos la columna 'los' en una variable aparte
LOS = final_df['los'].values
# Usamos todas las columnas excepto 'los' para usarlas como variables de entrada
features = final_df.drop(columns=['los'])

# Se entrena el modelo que se escogio
reg = GradientBoostingRegressor(random_state = 0)
reg.fit(features, LOS)

# # Se realiza la prediccion de los dias que la persona va a estar en la UCI
prediction = reg.predict(test)

st.write('La persona que ingreso a la UCI, durara un aproximado de ', int(prediction), ' dias')