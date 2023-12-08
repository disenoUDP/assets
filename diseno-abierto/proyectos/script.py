# importar modulo csv
import csv

# leer archivo .csv
with open('test.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row['Timestamp'])
    print(row['Nombre del taller'])
    print(row['Nombre del proyecto'])