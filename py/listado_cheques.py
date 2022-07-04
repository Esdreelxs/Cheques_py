import csv

cheque  = open("csv/listado.csv", "r")

dni = int(input("Ingrese el DNI: "))

salida = input("\nEscriba como desea visualizar los datos (PANTALLA o CSV): ")

tipo = input("\nTipo de cheque (EMITIDO o DEPOSITADO): ")

estado = input("\nEstado del cheque (PENDIENTE, APROBADO o RECHAZADO): ")

fecha = input("\nIngrese un rango de fechas (dd-mm-aaaa - dd-mm-aaaa): ")

if dni == 



#cheque.close