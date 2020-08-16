import json

def registros():
    def LeerJson():
        archivo = open("RegistrosJSON.json")  # Obtener acceso al archivo
        registros = json.load(archivo)  # Cargar datos del archivo
        archivo.close()  # Cerrar el flujo de datos
        return registros  # Retornar los datos obtenidos

    diccionario = LeerJson()  # Obtener los datos

    print("---------------------------------------------------------------------")
    print("                          REGISTROS JSON                              ")
    print("---------------------------------------------------------------------")

    i = 0
    for element in diccionario:  # Mostrar la lista
        i += 1
        print(f"* Registro: {i}")
        print(f"    {element}")

