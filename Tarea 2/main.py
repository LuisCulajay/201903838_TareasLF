import json
from xml.dom import minidom
import csv

#-----------------------------------------------------------------------------------------------------------------------

def LeerJson():
    archivo = open("RegistrosJSON.json")        #Obtener acceso al archivo
    registros = json.load(archivo)              #Cargar datos del archivo
    archivo.close()                             #Cerrar el flujo de datos
    return registros                            #Retornar los datos obtenidos

diccionario = LeerJson()                        #Obtener los datos

print("---------------------------------------------------------------------")
print("                          REGISTROS JSON                              ")
print("---------------------------------------------------------------------")

i = 0
for element in diccionario:                     #Mostrar la lista
    i+=1
    print(f"* Registro: {i}")
    print(f"    {element}")

#-----------------------------------------------------------------------------------------------------------------------

archivo = minidom.parse("RegistrosXML.xml")                                         #Obtener acceso al archivo y parsearlo
registros = archivo.getElementsByTagName("Usuario")                                 #Acceder a todos los registros con el tag Usuario

print("---------------------------------------------------------------------")
print("                          REGISTROS XML                              ")
print("---------------------------------------------------------------------")

for i in registros:

    NumeroRegistro = i.getAttribute("id")                       #Obtener el numero de identificador del registro actual
    nombre = i.getElementsByTagName("Nombre")[0]                #Obtener el nombre del registro actual
    universidad = i.getElementsByTagName("Universidad")[0]      #Obtener la universidad del registro actual
    facultad = i.getElementsByTagName("Facultad")[0]            #Obtener la facultad del registro actual
    ciclo = i.getElementsByTagName("Ciclo")[0]                  #Obtener el ciclo del registro actual

    print(f"* Registro No. {NumeroRegistro}")
    print(f"    Nombre: {nombre.firstChild.data}")
    print(f"    Universidad: {universidad.firstChild.data}")
    print(f"    Facultad: {facultad.firstChild.data}")
    print(f"    Ciclo: {ciclo.firstChild.data}")

#-----------------------------------------------------------------------------------------------------------------------

with open("RegistrosCSV.csv") as archivo:
    registros = csv.reader(archivo)

    NumeroRegistro = 0

    print("---------------------------------------------------------------------")
    print("                          REGISTROS CSV                              ")
    print("---------------------------------------------------------------------")

    for i in registros:
        NumeroRegistro +=1
        print(f"* Registro: {NumeroRegistro}")
        print(f"    Continente: {i[0]}")
        print(f"    País: {i[1]}")
        print(f"    Codigo de Área: {i[2]}")
        print(f"    Presidente: {i[3]}")