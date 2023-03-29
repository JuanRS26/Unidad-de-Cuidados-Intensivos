import mysql.connector

mydb = mysql.connector.connect(
  host="",   # Se pone la direccion IP donde se aloja la base de datos 
  user="",        # Se pone el nombre del usurio que hara las consultas a la base de datos 
  password="",    # Se pone la contraseña del usuario en caso que tenga una 
  database=""      # Se pone el nombre de la base de datos a la que se quiere hacer las consultas
)

mycursor = mydb.cursor()


'''------------------------------------Estructura para cargar los datos a la base de datos-----------------------------------------

for i in range(0, len(df)):                                       # Se crea un bucle for para entrar en cada uno de los registros de la tabla/dataframe
    sql = 'INSERT INTO `DF` VALUES (%S...)'                       # Se crea la estructura del INSERT con la cantidad de valores a ingresar
    val = (int(df.loc[i][0]), df.loc[i][1], ... , df.loc[i][n])   # se definen los valores para cada columna de cada registro 

    mycursor.execute(sql,val)                                     # Se ejecuta la consulta en la base de datos 

    mydb.commit()                                                 # Se guardan los cambios en la base de datos

---------------------------------------------------------------------------------------------------------------------------------'''


# PATIENTS

def tablePatients(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `PATIENTS` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), df.loc[i][2], df.loc[i][3], df.loc[i][4], df.loc[i][5], df.loc[i][6], int(df.loc[i][7]), float(df.loc[i][8]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de PATIENTS'


def selectTablePatients():
    sql = 'SELECT * FROM `PATIENTS`'

    mycursor.execute(sql)

    return mycursor


# D_ITEMS

def tableD_items(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `D_ITEMS` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), df.loc[i][2], df.loc[i][3], df.loc[i][4], df.loc[i][5], df.loc[i][6], df.loc[i][7], df.loc[i][8])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de D_ITEMS'


# D_LABITEMS

def tableD_labitems(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `D_LABITEMS` VALUES (%s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), df.loc[i][2], df.loc[i][3], df.loc[i][4], df.loc[i][5])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de D_LABITEMS'


# D_CPT

def tableD_CPT(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `D_CPT` VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), df.loc[i][2], df.loc[i][3], df.loc[i][4], df.loc[i][5], int(df.loc[i][6]), int(df.loc[i][7]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de D_CPT'


# D_ICD_DIAGNOSES

def tableD_icd_diagnoses(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `D_ICD_DIAGNOSES` VALUES (%s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de D_ICD_DIAGNOSES'


# D_ICD_PROCEDURES 

def tableD_icd_procedures(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `D_ICD_PROCEDURES` VALUES(%s, %s, %s, %s)'
        val = (int(df.loc[i][0]), str(df.loc[i][1]), df.loc[i][2], df.loc[i][3])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de D_ICD_PROCEDURES'


# CAREGIVERS

def tableCaregivers(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `CAREGIVERS` VALUES(%s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), df.loc[i][2], df.loc[i][3])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de CAREGIVERS'


# ADMISSIONS

def tableAdmissions(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `ADMISSIONS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), df.loc[i][3], df.loc[i][4], df.loc[i][5], df.loc[i][6], df.loc[i][7], df.loc[i][8], df.loc[i][9], df.loc[i][10], df.loc[i][11], df.loc[i][12], df.loc[i][13], df.loc[i][14], df.loc[i][15], df.loc[i][16], int(df.loc[i][17]), int(df.loc[i][18]), int(df.loc[i][19]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de ADMISSIONS'


def selectTableAdmissions():
    sql = 'SELECT * FROM `ADMISSIONS`'

    mycursor.execute(sql)

    return mycursor



# ICUSTAYS

def tableIcustays(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `ICUSTAYS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], df.loc[i][5], df.loc[i][6], int(df.loc[i][7]), int(df.loc[i][8]), df.loc[i][9], df.loc[i][10], float(df.loc[i][11]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de ICUSTAYS'


def selectTableIcustays():
    sql = 'SELECT * FROM `ICUSTAYS`'

    mycursor.execute(sql)

    return mycursor


# CALLOUT

def tableCallout(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `CALLOUT` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], int(df.loc[i][5]), df.loc[i][6], int(df.loc[i][7]), df.loc[i][8], int(df.loc[i][9]), int(df.loc[i][10]), int(df.loc[i][11]), int(df.loc[i][12]), int(df.loc[i][13]), df.loc[i][14], df.loc[i][15], int(df.loc[i][16]), df.loc[i][17], df.loc[i][18], df.loc[i][19], df.loc[i][20], df.loc[i][21], df.loc[i][22], df.loc[i][23])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de CALLOUT'


# CHARTEVENTS 

def tableChartevents(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `CHARTEVENTS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), int(df.loc[i][4]), df.loc[i][5], df.loc[i][6], int(df.loc[i][7]), int(df.loc[i][8]), df.loc[i][9], int(df.loc[i][10]), int(df.loc[i][11]), df.loc[i][12], df.loc[i][13])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de CHARTEVENTS'


# CPTEVENTS

def tableCptevents(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `CPTEVENTS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), str(df.loc[i][3]), df.loc[i][4], str(df.loc[i][5]), int(df.loc[i][6]), int(df.loc[i][7]), str(df.loc[i][8]), str(df.loc[i][9]), str(df.loc[i][10]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de CPTEVENTS'


# DATETIMEEVENTS  

def tableDatetimeevents(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `DATETIMEEVENTS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), int(df.loc[i][4]), df.loc[i][5], df.loc[i][6], int(df.loc[i][7]), df.loc[i][8], df.loc[i][9], int(df.loc[i][10]), int(df.loc[i][11]), df.loc[i][12])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de DATETIMEEVENTS'


# DIAGNOSES_ICD

def tableDiagnoses_icd(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `DIAGNOSES_ICD` VALUES(%s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de DIAGNOSES_ICD'


def selectTableDiagnoses_icd():
    sql = 'SELECT * FROM `DIAGNOSES_ICD`'

    mycursor.execute(sql)

    return mycursor


# DRGCODES

def tableDrgcodes(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `DRGCODES` VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), str(df.loc[i][3]), str(df.loc[i][4]), str(df.loc[i][5]), int(df.loc[i][6]), int(df.loc[i][7]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de DRGCODES'


# INPUTEVENTS_CV 

def tableInputevents_cv(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `INPUTEVENTS_CV` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], int(df.loc[i][5]), float(df.loc[i][6]), df.loc[i][7], df.loc[i][8], int(df.loc[i][9]), int(df.loc[i][10]), int(df.loc[i][11]), float(df.loc[i][12]), df.loc[i][13], df.loc[i][14])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de INPUTEVENTS_CV'


# INPUTEVENTS_MV

def tableInputevents_mv(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `INPUTEVENTS_MV` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], df.loc[i][5], int(df.loc[i][6]), float(df.loc[i][7]), df.loc[i][8], float(df.loc[i][9]), df.loc[i][10], df.loc[i][11], int(df.loc[i][12]), int(df.loc[i][13]), int(df.loc[i][14]), df.loc[i][15], df.loc[i][16], df.loc[i][17], df.loc[i][18], float(df.loc[i][19]), float(df.loc[i][20]), df.loc[i][21], int(df.loc[i][22]), int(df.loc[i][23]), int(df.loc[i][24]), df.loc[i][25], df.loc[i][26], float(df.loc[i][27]), float(df.loc[i][28]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de INPUTEVENTS_MV'


# LABEVENTS 

def tableLabevents(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `LABEVENTS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], float(df.loc[i][5]), df.loc[i][6], str(df.loc[i][7]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de LABEVENTS'


# MICROBIOLOGYEVENTS

def tableMicrobiologyevents(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `MICROBIOLOGYEVENTS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), df.loc[i][3], df.loc[i][4], int(df.loc[i][5]), df.loc[i][6], int(df.loc[i][7]), df.loc[i][8], int(df.loc[i][9]), int(df.loc[i][10]), df.loc[i][11], df.loc[i][12], df.loc[i][13], float(df.loc[i][14]), df.loc[i][15])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de MICROBIOLOGYEVENTS'


# OUTPUTEVENTS

def tableOutputevents(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `OUTPUTEVENTS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], int(df.loc[i][5]), float(df.loc[i][6]), df.loc[i][7], df.loc[i][8], int(df.loc[i][9]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de OUTPUTEVENTS'


# PRESCRIPTIONS

def tablePrescriptions(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `PRESCRIPTIONS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], df.loc[i][5], df.loc[i][6], df.loc[i][7], df.loc[i][8], df.loc[i][9], df.loc[i][10], df.loc[i][11], df.loc[i][12], df.loc[i][13], df.loc[i][14], df.loc[i][15], df.loc[i][16], df.loc[i][17], df.loc[i][18])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de PRESCRIPTIONS'


# PROCEDUREEVENTS_MV

def tableProcedureevents_mv(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `PROCEDUREEVENTS_MV` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], df.loc[i][5], int(df.loc[i][6]), float(df.loc[i][7]), str(df.loc[i][8]), df.loc[i][9], int(df.loc[i][10]), int(df.loc[i][11]), int(df.loc[i][12]), str(df.loc[i][13]), str(df.loc[i][14]), int(df.loc[i][15]), int(df.loc[i][16]), int(df.loc[i][17]), str(df.loc[i][18]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de PROCEDUREEVENTS_MV'


# PROCEDURES_ICD

def tableProcedures_icd(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `PROCEDURES_ICD` VALUES(%s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), str(df.loc[i][4]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de PROCEDURES_ICD'


# SERVICES

def tableServices(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `SERVICES` VALUES(%s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), df.loc[i][3], df.loc[i][4], df.loc[i][5])

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de SERVICES'


# TRANSFERS

def tableTransfers(df):
    for i in range(0, len(df)):
        sql = 'INSERT INTO `TRANSFERS` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (int(df.loc[i][0]), int(df.loc[i][1]), int(df.loc[i][2]), int(df.loc[i][3]), df.loc[i][4], df.loc[i][5], df.loc[i][6], df.loc[i][7], int(df.loc[i][8]), int(df.loc[i][9]), df.loc[i][10], df.loc[i][11], int(df.loc[i][12]))

        mycursor.execute(sql, val)

        mydb.commit()

    return '\nSe cargo exitosamente los datos de TRANSFERS'