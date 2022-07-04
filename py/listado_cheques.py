#prueba
#csv/listado.csv
#1617591371
#PANTALLA
#EMITIDO
#APROBADO

archivo = input("En que archivo desea buscar? ")
dni = int(input("Ingrese el DNI: "))
salida = input("Como desea visualizar los datos? ")
tipo = input("Tipo de cheque? ")
estado = input("Cual es el estado del cheque?(OPCIONAL) ")
rangFecha = input("Cual es el rango de fechas?(OPCIONAL) ")

import csv

with open('csv/listado.csv') as f:
    reader= csv.reader(f, delimiter=',')
    header = next(reader)
    if salida == "PANTALLA":
        for row in reader:
            i = 0
            dniCVS = []
            tipoCSV = []
            estadoCSV = []
            dniCVS.append(int(row[8]))
            tipoCSV.append(row[9])
            estadoCSV.append(row[10])
           if dniCSV[i] == dni:
                if tipoCSV[i] == tipo:
                    if estadoCSV[i] == estado:
                        print("NroCheque: {0},CodigoBanco: {1},CodigoScurusal: {2},NumeroCuentaOrigen: {3},NumeroCuentaDestino: {4},Valor: {5},FechaOrigen: {6},FechaPago: {7},DNI: {8},Tipo: {9},Estado:{10}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
                    else:
                        print("NroCheque: {0},CodigoBanco: {1},CodigoScurusal: {2},NumeroCuentaOrigen: {3},NumeroCuentaDestino: {4},Valor: {5},FechaOrigen: {6},FechaPago: {7},DNI: {8},Tipo: {9},Estado:{10}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
           i += 1
    elif salida == "CSV":
        import csv # COMPLETAR
#cheque.close
