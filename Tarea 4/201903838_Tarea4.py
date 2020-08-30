import webbrowser

objetos = list()        #Crear la lista que guardará todos los objetos
def llenarListas():
    objetos.append("Registro 1")
    objetos.append("Registro 2")
    objetos.append("Registro 3")
    objetos.append("Registro 4")
    objetos.append("Registro 5")
    objetos.append("Registro 6")
    objetos.append("Registro 7")
    objetos.append("Registro 8")
    objetos.append("Registro 9")
    objetos.append("Registro 10")

    objetos[0] = list()
    objetos[1] = list()
    objetos[2] = list()
    objetos[3] = list()
    objetos[4] = list()
    objetos[5] = list()
    objetos[6] = list()
    objetos[7] = list()
    objetos[8] = list()
    objetos[9] = list()

    #Llenar primer atributo "nombre" de cada registro
    objetos[0].append("Marco")
    objetos[1].append("Antonio")
    objetos[2].append("Amarilys")
    objetos[3].append("Fabiola")
    objetos[4].append("Karen")
    objetos[5].append("Carlos")
    objetos[6].append("Andres")
    objetos[7].append("Juan")
    objetos[8].append("Mario")
    objetos[9].append("Felipe")
    # Llenar segundo atributo "edad" de cada registro
    objetos[0].append("50")
    objetos[1].append("43")
    objetos[2].append("55")
    objetos[3].append("67")
    objetos[4].append("32")
    objetos[5].append("23")
    objetos[6].append("40")
    objetos[7].append("3")
    objetos[8].append("77")
    objetos[9].append("14")
    # Llenar tercer atributo "activo" de cada registro
    objetos[0].append("True")
    objetos[1].append("True")
    objetos[2].append("True")
    objetos[3].append("False")
    objetos[4].append("True")
    objetos[5].append("False")
    objetos[6].append("False")
    objetos[7].append("True")
    objetos[8].append("False")
    objetos[9].append("True")
    # Llenar cuarto atributo "saldo" de cada registro
    objetos[0].append("Q.100")
    objetos[1].append("Q.200")
    objetos[2].append("Q.300")
    objetos[3].append("Q.150")
    objetos[4].append("Q.250")
    objetos[5].append("Q.350")
    objetos[6].append("Q.400")
    objetos[7].append("Q.10")
    objetos[8].append("Q.70")
    objetos[9].append("Q.3000")
def generarHTML():
    print("***** REPORTE EN HTML *****")

    documento = open('index.html', 'w')         #Abrir una conexion al documento .html

    # Codigo a escribir que siempre esta fijo
    mensaje = """               
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="estilo.css">
        <title>SIMPLE QL</title>
    </head>

    <body>
        <h1>REPORTE SIMPLE QL</h1>
        <div id="tabla"> 
        <table>
            <thead>
                <tr>
                    <th>NOMBRE</th>
                    <th>EDAD</th>
                    <th>ACTIVO</th>
                    <th>SALDO</th>
                </tr>
            </thead>
            <tbody>"""

    for indice in range(0, 10):         #Ciclo que recorre desde 0 hasta la cantidad de reportes requeridos - 1
        mensaje = mensaje + "<tr>"      #Etiqueta que abre cada fila/registro
        for posicion in range(0,4):     #Ciclo que recorre el interior de cada elemento -1
            mensaje = mensaje + "<td>" + str(objetos[indice][posicion]) + "</td>"  #Armar todas las columnas una a una "nombre,edad,activo,saldo"
        mensaje = mensaje + "</tr>"     #Etiqueta que cierra cada fila/registro

    mensaje = mensaje + "</tbody></table></div></body></html>"  #Terminar de concatenar las etiquetas de cierre del documento

    documento.write(mensaje)    #Escribir el mensaje en index.html
    documento.close()           #Cerrar el documento

    webbrowser.open(            #Abrir documento en el explorador
        'index.html'
    )

llenarListas()
generarHTML()