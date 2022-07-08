#prueba
#csv/listado.csv
#1617591371
#PANTALLA
#EMITIDO
#APROBADO

import csv
import sys
import datetime

print(sys.argv[0])

archivo = input("\nEn que archivo desea buscar?\n")
dni = input("\nIngrese el DNI:\n")
salida = input("\nEscriba como desea visualizar los datos (PANTALLA o CSV):\n")
tipo = input("\nTipo de cheque (EMITIDO o DEPOSITADO):\n")
estado = input("\nEstado del cheque (PENDIENTE, APROBADO o RECHAZADO)(opcional):\n")
rangFecha = input("\nIngrese un rango de fechas (dd-mm-aaaa:dd-mm-aaaa)(opcional):\n")

date1 = rangFecha[0:10]
date1 = datetime.datetime.strptime(date1,r"%d-%m-%Y")
date1 = datetime.datetime.timestamp(date1)
date2 = rangFecha[11:21]
date2 = datetime.datetime.strptime(date2,r"%d-%m-%Y")
date2 = datetime.datetime.timestamp(date2)

with open(archivo) as f:
    reader= csv.reader(f, delimiter=',')
    header = next(reader)
    if salida == "PANTALLA":
        for row in reader:
            i = 0
            dniCSV = []
            tipoCSV = []
            estadoCSV = []
            fechaOrCSV = []
            fechaPgCSV = []
            dniCSV.append(row[8])
            tipoCSV.append(row[9])
            estadoCSV.append(row[10])
            fechaOrCSV.append(float(row[6]))
            fechaPgCSV.append(float(row[7]))
            if dniCSV[i] == dni:
                if tipoCSV[i] == tipo:
                    if estadoCSV[i] == estado or estado == '':
                        if (fechaOrCSV[i] >= date1 and fechaPgCSV[i] <= date2) or rangFecha == '':
                            print("NroCheque: {0},CodigoBanco: {1},CodigoScurusal: {2},NumeroCuentaOrigen: {3},NumeroCuentaDestino: {4},Valor: {5},FechaOrigen: {6},FechaPago: {7},DNI: {8},Tipo: {9},Estado:{10}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))

    elif salida == "CSV":
        now = datetime.datetime.now()
        date_time = now.strftime(r"%d-%m-%Y_%H.%M.%S")      
        with open(('csv/' + dni + '_' + date_time + '.csv'), "w") as f:
                    f.write(sys.argv[2])

    else:
        print("Argumento invalido")
                
        exit(1)


        
#cheque.close
