import pandas as pd
import ETL_Functions as ef
import LoadDB as db

def incremental():

    flag = False

    print(f'\n1) ADMISSIONS \n2) CALLOUT \n3) CAREGIVERS \n4) CHARTEVENTS \n5) CPTEVENTS \n6) D_CPT \
        \n7) D_ICD_DIAGNOSES\n8) D_ICD_PROCEDURES\n9) D_ITEMS\n10) D_LABITEMS\n11) DATETIMEEVENTS \
        \n12) DIAGNOSES_ICD\n13) DRGCODES\n14) ICUSTAYS\n15) INPUTEVENTS_CV\n16) INPUTEVENTS_MV \
        \n17) LABEVENTS\n18) MICROBIOLOGYEVENTS\n19) OUTPUTEVENTS\n20) PATIENTS\n21) PRESCRIPTIONS \
        \n22) PROCEDUREEVENTS_MV\n23) PROCEDURES_ICD\n24) SERVICES\n25) TRANSFERS')
    print('\nPor favor, aloje el archivo "csv" con el respectivo nombre de la tabla en la carpeta "Updates"')

    opc = input('\nDigite el numero de la tabla a la cual desea ingresar datos: ')

    while flag == False:
        if opc == '1':
            ADMISSIONS = pd.read_csv('Updates/ADMISSIONS.csv')
            ADMISSIONS = ef.etl_admissions(ADMISSIONS)
            response = db.tableAdmissions(ADMISSIONS)
            print(response)
            flag = True
        elif opc == '2':
            CALLOUT = pd.read_csv('Updates/CALLOUT.csv')
            CALLOUT = ef.etl_callout(CALLOUT)
            response = db.tableCallout(CALLOUT)
            print(response)
            flag = True
        elif opc == '3':
            CAREGIVERS = pd.read_csv('Updates/CAREGIVERS.csv')
            CAREGIVERS = ef.etl_caregivers(CAREGIVERS)
            response = db.tableCaregivers(CAREGIVERS)
            print(response)
            flag = True
        elif opc == '4':
            CHARTEVENTS = pd.read_csv('Updates/CHARTEVENTS.csv')
            CHARTEVENTS = ef.etl_chartevents(CHARTEVENTS)
            response = db.tableChartevents(CHARTEVENTS)
            print(response)
            flag = True
        elif opc == '5':
            CPTEVENTS = pd.read_csv('Updates/CPTEVENTS.csv')
            CPTEVENTS = ef.etl_cptevents(CPTEVENTS)
            response = db.tableCptevents(CPTEVENTS)
            print(response)
            flag = True
        elif opc == '6':
            D_CPT = pd.read_csv('Updates/D_CPT.csv')
            D_CPT = ef.etl_d_cpt(D_CPT)
            response = db.tableD_CPT(D_CPT)
            print(response)
            flag = True
        elif opc == '7':
            D_ICD_DIAGNOSES = pd.read_csv('Updates/D_ICD_DIAGNOSES.csv')
            D_ICD_DIAGNOSES = ef.etl_d_icd_diagnoses(D_ICD_DIAGNOSES)
            response = db.tableD_icd_diagnoses(D_ICD_DIAGNOSES)
            print(response)
            flag = True
        elif opc == '8':
            D_ICD_PROCEDURES = pd.read_csv('Updates/D_ICD_PROCEDURES.csv')
            D_ICD_PROCEDURES = ef.etl_d_icd_procedures(D_ICD_PROCEDURES)
            response = db.tableD_icd_procedures(D_ICD_PROCEDURES)
            print(response)
            flag = True
        elif opc == '9':
            D_ITEMS = pd.read_csv('Updates/D_ITEMS.csv')
            D_ITEMS = ef.etl_d_items(D_ITEMS)
            response = db.tableD_items(D_ITEMS)
            print(response)
            flag = True
        elif opc == '10':
            D_LABITEMS = pd.read_csv('Updates/D_LABITEMS.csv')
            D_LABITEMS = ef.etl_d_labitem(D_LABITEMS)
            response = db.tableD_labitems(D_LABITEMS)
            print(response)
            flag = True
        elif opc == '11':
            DATETIMEEVENTS = pd.read_csv('Updates/DATETIMEEVENTS.csv')
            DATETIMEEVENTS = ef.etl_datetimeevents(DATETIMEEVENTS)
            response = db.tableDatetimeevents(DATETIMEEVENTS)
            print(response)
            flag = True
        elif opc == '12':
            DIAGNOSES_ICD = pd.read_csv('Updates/DIAGNOSES_ICD.csv')
            DIAGNOSES_ICD = ef.etl_diagnoses_icd(DIAGNOSES_ICD)
            response = db.tableDiagnoses_icd(DIAGNOSES_ICD)
            print(response)
            flag = True
        elif opc == '13':
            DRGCODES = pd.read_csv('Updates/DRGCODES.csv')
            DRGCODES = ef.etl_drgcodes(DRGCODES)
            response = db.tableDrgcodes(DRGCODES)
            print(response)
            flag = True
        elif opc == '14':
            ICUSTAYS = pd.read_csv('Updates/ICUSTAYS.csv')
            ICUSTAYS = ef.etl_icustays(ICUSTAYS)
            response = db.tableIcustays(ICUSTAYS)
            print(response)
            flag = True
        elif opc == '15':
            INPUTEVENTS_CV = pd.read_csv('Updates/INPUTEVENTS_CV.csv')
            INPUTEVENTS_CV = ef.etl_inputevents_cv(INPUTEVENTS_CV)
            response = db.tableInputevents_cv(INPUTEVENTS_CV)
            print(response)
            flag = True
        elif opc == '16':
            INPUTEVENTS_MV = pd.read_csv('Updates/INPUTEVENTS_MV.csv')
            INPUTEVENTS_MV = ef.etl_inputevents_mv(INPUTEVENTS_MV)
            response = db.tableInputevents_mv(INPUTEVENTS_MV)
            print(response)
            flag = True
        elif opc == '17':
            LABEVENTS = pd.read_csv('Updates/LABEVENTS.csv')
            LABEVENTS = ef.etl_labevents(LABEVENTS)
            response = db.tableLabevents(LABEVENTS)
            print(response)
            flag = True
        elif opc == '18':
            MICROBIOLOGYEVENTS = pd.read_csv('Updates/MICROBIOLOGYEVENTS.csv')
            MICROBIOLOGYEVENTS = ef.etl_micriobiologyevents(MICROBIOLOGYEVENTS)
            response = db.tableMicrobiologyevents(MICROBIOLOGYEVENTS)
            print(response)
            flag = True
        elif opc == '19':
            OUTPUTEVENTS = pd.read_csv('Updates/OUTPUTEVENTS.csv')
            OUTPUTEVENTS = ef.etl_outputevents(OUTPUTEVENTS)
            response = db.tableOutputevents(OUTPUTEVENTS)
            print(response)
            flag = True
        elif opc == '20':
            PATIENTS = pd.read_csv('Updates/PATIENTS.csv')
            PATIENTS = ef.etl_patients(PATIENTS)
            response = db.tablePatients(PATIENTS)
            print(response)
            flag = True
        elif opc == '21':
            PRESCRIPTIONS = pd.read_csv('Updates/PRESCRIPTIONS.csv')
            PRESCRIPTIONS = ef.etl_prescriptions(PRESCRIPTIONS)
            response = db.tablePrescriptions(PRESCRIPTIONS)
            print(response)
            flag = True
        elif opc == '22':
            PROCEDUREEVENTS_MV = pd.read_csv('Updates/PROCEDUREEVENTS_MV.csv')
            PROCEDUREEVENTS_MV = ef.etl_procedureevents_mv(PROCEDUREEVENTS_MV)
            response = db.tableProcedureevents_mv(PROCEDUREEVENTS_MV)
            print(response)
            flag = True
        elif opc == '23':
            PROCEDURES_ICD = pd.read_csv('Updates/PROCEDURES_ICD.csv')
            PROCEDURES_ICD = ef.etl_procedures_icd(PROCEDURES_ICD)
            response = db.tableProcedures_icd(PROCEDURES_ICD)
            print(response)
            flag = True
        elif opc == '24':
            SERVICES = pd.read_csv('Updates/SERVICES.csv')
            SERVICES = ef.etl_services(SERVICES)
            response = db.tableServices(SERVICES)
            print(response)
            flag = True
        elif opc == '25':
            TRANSFERS = pd.read_csv('Updates/TRANSFERS.csv')
            TRANSFERS = ef.etl_transfers(TRANSFERS)
            response = db.tableTransfers(TRANSFERS)
            print(response)
            flag = True
        else:
            opc = input('Opcion incorrecta, ingresa una de las opciones que se encuentran: ')