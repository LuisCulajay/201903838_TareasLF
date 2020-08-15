#todo dentro de corchetes es una lista
#todo dentro de llaves es un objeto

import json

def readJson():     #Definir una funcion
    file = open("RegistrosJSON.json")
    data = json.load(file)
    file.close()
    return data

diccionario = readJson()
for element in diccionario:
    print(element)