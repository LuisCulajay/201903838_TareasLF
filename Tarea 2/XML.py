from xml.dom import minidom

def registros():
    archivo = minidom.parse("RegistrosXML.xml")  # Obtener acceso al archivo y parsearlo
    registros = archivo.getElementsByTagName("Usuario")  # Acceder a todos los registros con el tag Usuario

    print("---------------------------------------------------------------------")
    print("                          REGISTROS XML                              ")
    print("---------------------------------------------------------------------")

    for i in registros:
        NumeroRegistro = i.getAttribute("id")  # Obtener el numero de identificador del registro actual
        nombre = i.getElementsByTagName("Nombre")[0]  # Obtener el nombre del registro actual
        universidad = i.getElementsByTagName("Universidad")[0]  # Obtener la universidad del registro actual
        facultad = i.getElementsByTagName("Facultad")[0]  # Obtener la facultad del registro actual
        ciclo = i.getElementsByTagName("Ciclo")[0]  # Obtener el ciclo del registro actual

        print(f"* Registro No. {NumeroRegistro}")
        print(f"    Nombre: {nombre.firstChild.data}")
        print(f"    Universidad: {universidad.firstChild.data}")
        print(f"    Facultad: {facultad.firstChild.data}")
        print(f"    Ciclo: {ciclo.firstChild.data}")