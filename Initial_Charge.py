import pandas as pd
import LoadDB as db
import ETL_Functions as ef

def initial():

    # PATIENTS

    PATIENTS = pd.read_csv('Datasets/Normal/PATIENTS.csv')    # Se cargan los datos sin transformaciones
    PATIENTS = ef.etl_patients(PATIENTS)    # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    PATIENTS.to_csv('Datasets/Transformations/PATIENTS_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tablePatients(PATIENTS)   # Se cargan a la base de datos 
    print(response)


    # D_ITEMS

    D_ITEMS = pd.read_csv('Datasets/Normal/D_ITEMS.csv')  # Se cargan los datos sin transformaciones
    D_ITEMS = ef.etl_d_items(D_ITEMS)   # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    D_ITEMS.to_csv('Datasets/Transformations/D_ITEMS_C.csv', index=False)   # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableD_items(D_ITEMS) # Se cargan a la base de datos 
    print(response)


    # D_LABITEMS

    D_LABITEMS = pd.read_csv('Datasets/Normal/D_LABITEMS.csv')    # Se cargan los datos sin transformaciones
    D_LABITEMS = ef.etl_d_labitem(D_LABITEMS)   # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    D_LABITEMS.to_csv('Datasets/Transformations/D_LABITEMS_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableD_labitems(D_LABITEMS)   # Se cargan a la base de datos 
    print(response)


    # D_CPT

    D_CPT = pd.read_csv('Datasets/Normal/D_CPT.csv')  # Se cargan los datos sin transformaciones
    D_CPT = ef.etl_d_cpt(D_CPT) # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    D_CPT.to_csv('Datasets/Transformations/D_CPT_C.csv', index=False)   # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableD_CPT(D_CPT) # Se cargan a la base de datos 
    print(response)


    # D_ICD_DIAGNOSES

    D_ICD_DIAGNOSES = pd.read_csv('Datasets/Normal/D_ICD_DIAGNOSES.csv')  # Se cargan los datos sin transformaciones
    D_ICD_DIAGNOSES = ef.etl_d_icd_diagnoses(D_ICD_DIAGNOSES)   # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    D_ICD_DIAGNOSES.to_csv('Datasets/Transformations/D_ICD_DIAGNOSES_C.csv', index = False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableD_icd_diagnoses(D_ICD_DIAGNOSES) # Se cargan a la base de datos 
    print(response)


    # D_ICD_PROCEDURES

    D_ICD_PROCEDURES = pd.read_csv('Datasets/Normal/D_ICD_PROCEDURES.csv')    # Se cargan los datos sin transformaciones
    D_ICD_PROCEDURES = ef.etl_d_icd_procedures(D_ICD_PROCEDURES)    # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    D_ICD_PROCEDURES.to_csv('Datasets/Transformations/D_ICD_PROCEDURES_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableD_icd_procedures(D_ICD_PROCEDURES)   # Se cargan a la base de datos 
    print(response)


    # CAREGIVERS

    CAREGIVERS = pd.read_csv('Datasets/Normal/CAREGIVERS.csv')    # Se cargan los datos sin transformaciones
    CAREGIVERS = ef.etl_caregivers(CAREGIVERS)  # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    CAREGIVERS.to_csv('Datasets/Transformations/CAREGIVERS_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableCaregivers(CAREGIVERS)   # Se cargan a la base de datos 
    print(response)
            

    # ADMISSIONS

    ADMISSIONS = pd.read_csv('Datasets/Normal/ADMISSIONS.csv')    # Se cargan los datos sin transformaciones
    ADMISSIONS = ef.etl_admissions(ADMISSIONS)  # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    ADMISSIONS.to_csv('Datasets/Transformations/ADMISSIONS_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableAdmissions(ADMISSIONS)   # Se cargan a la base de datos 
    print(response)


    # ICUSTAYS

    ICUSTAYS = pd.read_csv('Datasets/Normal/ICUSTAYS.csv')    # Se cargan los datos sin transformaciones
    ICUSTAYS = ef.etl_icustays(ICUSTAYS)    # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    ICUSTAYS.to_csv('Datasets/Transformations/ICUSTAYS_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableIcustays(ICUSTAYS)   # Se cargan a la base de datos 
    print(response)


    # CALLOUT

    CALLOUT = pd.read_csv('Datasets/Normal/CALLOUT.csv')  # Se cargan los datos sin transformaciones
    CALLOUT = ef.etl_callout(CALLOUT)   # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    CALLOUT.to_csv('Datasets/Transformations/CALLOUT_C.csv', index=False)   # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableCallout(CALLOUT) # Se cargan a la base de datos 
    print(response)


    # # CHARTEVENTS

    # CHARTEVENTS = pd.read_csv('Datasets/Normal/CHARTEVENTS.csv')  # Se cargan los datos sin transformaciones
    # CHARTEVENTS = ef.etl_chartevents(CHARTEVENTS)   # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    # CHARTEVENTS.to_csv('Datasets/Transformations/CHARTEVENTS_C.csv', index=False)   # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    # response = db.tableChartevents(CHARTEVENTS) # Se cargan a la base de datos 
    # print(response)


    # CPTEVENTS

    CPTEVENTS = pd.read_csv('Datasets/Normal/CPTEVENTS.csv')  # Se cargan los datos sin transformaciones
    CPTEVENTS = ef.etl_cptevents(CPTEVENTS) # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    CPTEVENTS.to_csv('Datasets/Transformations/CPTEVENTS_C.csv', index=False)   # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableCptevents(CPTEVENTS) # Se cargan a la base de datos 
    print(response)


    # DATETIMEEVENTS

    DATETIMEEVENTS = pd.read_csv('Datasets/Normal/DATETIMEEVENTS.csv')    # Se cargan los datos sin transformaciones
    DATETIMEEVENTS = ef.etl_datetimeevents(DATETIMEEVENTS)  # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    DATETIMEEVENTS.to_csv('Datasets/Transformations/DATETIMEEVENTS_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableDatetimeevents(DATETIMEEVENTS)   # Se cargan a la base de datos 
    print(response)


    # DIAGNOSES_ICD

    DIAGNOSES_ICD = pd.read_csv('Datasets/Normal/DIAGNOSES_ICD.csv')  # Se cargan los datos sin transformaciones
    DIAGNOSES_ICD = ef.etl_diagnoses_icd(DIAGNOSES_ICD) # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    DIAGNOSES_ICD.to_csv('Datasets/Transformations/DIAGNOSES_ICD_C.csv', index = False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableDiagnoses_icd(DIAGNOSES_ICD) # Se cargan a la base de datos 
    print(response)
            

    # DRGCODES

    DRGCODES = pd.read_csv('Datasets/Normal/DRGCODES.csv')    # Se cargan los datos sin transformaciones
    DRGCODES = ef.etl_drgcodes(DRGCODES)    # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    DRGCODES.to_csv('Datasets/Transformations/DRGCODES_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableDrgcodes(DRGCODES)   # Se cargan a la base de datos 
    print(response)
    

    # INPUTEVENTS_CV

    INPUTEVENTS_CV = pd.read_csv('Datasets/Normal/INPUTEVENTS_CV.csv')    # Se cargan los datos sin transformaciones
    INPUTEVENTS_CV = ef.etl_inputevents_cv(INPUTEVENTS_CV)  # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    INPUTEVENTS_CV.to_csv('Datasets/Transformations/INPUTEVENTS_CV_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableInputevents_cv(INPUTEVENTS_CV)   # Se cargan a la base de datos 
    print(response)
            

    # INPUTEVENTS_MV

    INPUTEVENTS_MV = pd.read_csv('Datasets/Normal/INPUTEVENTS_MV.csv')    # Se cargan los datos sin transformaciones
    INPUTEVENTS_MV = ef.etl_inputevents_mv(INPUTEVENTS_MV)  # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    INPUTEVENTS_MV.to_csv('Datasets/Transformations/INPUTEVENTS_MV_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableInputevents_mv(INPUTEVENTS_MV)   # Se cargan a la base de datos 
    print(response)
            

    # LABEVENTS

    LABEVENTS = pd.read_csv('Datasets/Normal/LABEVENTS.csv')  # Se cargan los datos sin transformaciones
    LABEVENTS = ef.etl_labevents(LABEVENTS) # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    LABEVENTS.to_csv('Datasets/Transformations/LABEVENTS_C.csv', index=False)   # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableLabevents(LABEVENTS) # Se cargan a la base de datos 
    print(response)
            

    # MICROBIOLOGYEVENTS

    MICROBIOLOGYEVENTS = pd.read_csv('Datasets/Normal/MICROBIOLOGYEVENTS.csv')    # Se cargan los datos sin transformaciones
    MICROBIOLOGYEVENTS = ef.etl_micriobiologyevents(MICROBIOLOGYEVENTS) # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    MICROBIOLOGYEVENTS.to_csv('Datasets/Transformations/MICROBIOLOGYEVENTS_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableMicrobiologyevents(MICROBIOLOGYEVENTS)   # Se cargan a la base de datos 
    print(response)
            

    # OUTPUTEVENTS

    OUTPUTEVENTS = pd.read_csv('Datasets/Normal/OUTPUTEVENTS.csv')    # Se cargan los datos sin transformaciones
    OUTPUTEVENTS = ef.etl_outputevents(OUTPUTEVENTS)    # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    OUTPUTEVENTS .to_csv('Datasets/Transformations/OUTPUTEVENTS _C.csv', index=False)   # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableOutputevents(OUTPUTEVENTS)   # Se cargan a la base de datos 
    print(response)


    # PRESCRIPTIONS

    PRESCRIPTIONS = pd.read_csv('Datasets/Normal/PRESCRIPTIONS.csv')  # Se cargan los datos sin transformaciones
    PRESCRIPTIONS = ef.etl_prescriptions(PRESCRIPTIONS) # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    PRESCRIPTIONS.to_csv('Datasets/Transformations/PRESCRIPTIONS_C.csv', index = False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tablePrescriptions(PRESCRIPTIONS) # Se cargan a la base de datos 
    print(response)
            

    # PROCEDUREEVENTS_MV

    PROCEDUREEVENTS_MV = pd.read_csv('Datasets/Normal/PROCEDUREEVENTS_MV.csv')    # Se cargan los datos sin transformaciones
    PROCEDUREEVENTS_MV = ef.etl_procedureevents_mv(PROCEDUREEVENTS_MV)  # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    PROCEDUREEVENTS_MV.to_csv('Datasets/Transformations/PROCEDUREEVENTS_MV_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableProcedureevents_mv(PROCEDUREEVENTS_MV)   # Se cargan a la base de datos 
    print(response)
            

    # PROCEDURES_ICD

    PROCEDURES_ICD = pd.read_csv('Datasets/Normal/PROCEDURES_ICD.csv')    # Se cargan los datos sin transformaciones
    PROCEDURES_ICD = ef.etl_procedures_icd(PROCEDURES_ICD)  # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    PROCEDURES_ICD.to_csv('Datasets/Transformations/PROCEDURES_ICD_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableProcedures_icd(PROCEDURES_ICD)   # Se cargan a la base de datos 
    print(response)
            

    # SERVICES

    SERVICES = pd.read_csv('Datasets/Normal/SERVICES.csv')    # Se cargan los datos sin transformaciones
    SERVICES = ef.etl_services(SERVICES)    # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    SERVICES.to_csv('Datasets/Transformations/SERVICES_C.csv', index=False) # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableServices(SERVICES)   # Se cargan a la base de datos 
    print(response)


    # TRANSFERS

    TRANSFERS = pd.read_csv('Datasets/Normal/TRANSFERS.csv')    # Se cargan los datos sin transformaciones
    TRANSFERS = ef.etl_transfers(TRANSFERS) # Se realiza el proceso de limpieza de los datos para subirlos a la base de datos
    TRANSFERS.to_csv('Datasets/Transformations/TRANSFERS_C.csv', index=False)   # Se guardan los datos en un archivo 'csv' luego de hacer la limpieza
    response = db.tableTransfers(TRANSFERS) # Se cargan a la base de datos 
    print(response)