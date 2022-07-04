import csv

with open('csv/listado.csv') as f:
    reader= csv.reader(f, delimiter=',')
    for row in reader:
        print("NroCheque: {0},CodigoBanco: {1},CodigoScurusal: {2},NumeroCuentaOrigen: {3},NumeroCuentaDestino: {4},Valor: {5},FechaOrigen: {6},FechaPago: {7},DNI: {8},Tipo: {9},Estado:{10}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))






#cheque  = open(".../csv/listado.csv40", "w")
#dni = int(input("Ingrese el DNI: "))
#salida = input("\nComo desea visualizar los datos?(PANTALLA o CSV): ")
#tipo = input("Tipo de cheque?")






#cheque.close