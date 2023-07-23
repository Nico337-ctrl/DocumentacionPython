#importando el modulo csv
import csv

with open('ArchivosCSV\\archivo.csv') as archivo:
    #leyendo un archivo csv
    #print(csv.reader(archivo))
    

    #recorriendo un archivo csv

    leer = csv.reader(archivo)
    for i in leer:
        print(i)
