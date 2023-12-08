# importar modulos
import csv
import json

# crear lista vacia
lista = []

# leer archivo .csv
with open('test.csv', newline='', encoding='utf-8') as csvfile:
  # crear objeto lector en formato diccionario
  reader = csv.DictReader(csvfile)

  # por cada fila del archivo
  for row in reader:

    # crear diccionario en blanco
    diccionario = {}
    # agregar items
    diccionario['timestamp'] = row['Timestamp']
    diccionario['sigla'] = row['Nombre del taller'].split(' ')[0]
    diccionario['nombre'] = row['Nombre del proyecto']
    diccionario['estudiantes'] = row['Nombres completos'].split(', ')
    diccionario['texto'] = row['Texto explicativo']
    diccionario['etiquetas'] = row['Etiquetas'].split(', ')
    # diccionario['Imagenes'] = row['Imagenes'].split(', ')
    diccionario['url'] = 'https://placehold.co/400'
    diccionario['thumbnailURL'] = 'https://placehold.co/400'

    # agregar diccionario a lista
    lista.append(diccionario)
    

# Serializing json
json_object = json.dumps(lista, indent=2)
 
# Writing to sample.json
with open("proyectos.json", "w", encoding='utf-8') as outfile:
    outfile.write(json_object)