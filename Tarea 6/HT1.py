cadena = """(
    <
        [atributo_numerico] = 45.09,
        [atributo_cadena] = "hola mundo",
        [atributo_booleano] = true
    >,
    <
        [atributo_numerico] = 4,
        [atributo_cadena] = "adios mundo",
        [atributo_booleano] = false
    >,
    <
        [atributo_numerico] = -56.4,
        [atributo_cadena] = "este es otro ejemplo, las cadenas pueden ser muy largas",
        [atributo_booleano] = false
    >
)"""
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z')
numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '-')

tk_Simbolos = list()
tk_Atributo = list()
tk_Numero = list()
tk_Cadena = list()
tk_Boolean = list()


def esLetra(letra):
    for caracter in letras:
        if letra == caracter:
            return True

    return False
def esNumero(numero):
    for digito in numeros:
        if numero == str(digito):
            return True

    return False
def automata(cadena):
    estado = 0
    palabra = ""
    comillasEncontradas = False

    cadena = cadena.lower()
    for letra in cadena:
        if estado == 0:
            if letra == "(":
                print(f"{letra}: tk_ParentesisApertura")
                tk_Simbolos.append(letra)
                estado = 1
        elif estado == 1:
            if letra == ",":
                estado = 1
                print(f"{letra}: tk_Coma")
                tk_Simbolos.append(letra)
            elif letra == "<":
                estado = 2
                print(f"{letra}: tk_MenorQue")
                tk_Simbolos.append(letra)
            elif letra == ")":
                print(f"{letra}: tk_ParentesisCierre")
                tk_Simbolos.append(letra)
                return
        elif estado == 2:
            if letra == "[":
                estado = 3
                print(f"{letra}: tk_LlaveApertura")
                tk_Simbolos.append(letra)
        elif estado == 3:
            if letra == "]":
                print(f"{palabra}: tk_Atributo")
                tk_Atributo.append(palabra)
                palabra = ""

                estado = 4
                print(f"{letra}: tk_LLaveCierre")
                tk_Simbolos.append(letra)
            else:
                palabra += letra
                estado = 3
        elif estado == 4:
            if letra == "=":
                estado = 5
                print(f"{letra}: tk_Igual")
                tk_Simbolos.append(letra)
        elif estado == 5:
            if ord(letra) == 34:
                estado = 6
                print(f"{letra}: tk_Comillas")
                tk_Simbolos.append(letra)
            elif esNumero(letra) == True:
                palabra += letra
                estado = 7
            elif esLetra(letra) == True:
                palabra += letra
                estado = 8
        elif estado == 6:
            if ord(letra) == 34:
                comillasEncontradas = True              #Hasta que se encontraron las dos comillas dejar de concatenar
                print(f"{palabra}: tk_Cadena")
                tk_Cadena.append(palabra)
                palabra=""

                print(f"{letra}: tk_Comillas")
                tk_Simbolos.append(letra)

            if comillasEncontradas == False:
                palabra += letra
            else:
                if letra == ",":
                    comillasEncontradas = False         #Reiniciar la variable de comillas encontradas
                    tk_Simbolos.append(letra)
                    estado = 2
                    print(f"{letra}: tk_Coma")

                elif letra == ">":
                    comillasEncontradas = False         #Reiniciar la variable de comillas encontradas
                    estado = 1
                    tk_Simbolos.append(letra)
                    print(f"{letra}: tk_MayorQue")
#
        elif estado == 7:
            if letra == ",":
                print(f"{palabra}: tk_Numero")
                tk_Numero.append(palabra)
                palabra = ""

                estado = 2
                tk_Simbolos.append(letra)
                print(f"{letra}: tk_Coma")
            elif letra == ">":
                print(f"{palabra}: tk_Numero")
                tk_Numero.append(palabra)
                palabra = ""

                estado = 1
                tk_Simbolos.append(letra)
                print(f"{letra}: tk_MayorQue")
            else:
                if esNumero(letra):            #Guardar sino es un salto de linea
                    palabra += letra
        elif estado == 8:
            if letra == ",":
                print(f"{palabra}: tk_Boolean")
                tk_Boolean.append(palabra)
                palabra = ""

                estado = 2
                tk_Simbolos.append(letra)
                print(f"{letra}: tk_Coma")
            elif letra == ">":
                print(f"{palabra}: tk_Boolean")
                tk_Boolean.append(palabra)
                palabra = ""

                estado = 1
                tk_Simbolos.append(letra)
                print(f"{letra}: tk_MayorQue")
            else:
                if esLetra(letra):              #Guardar sino es un salto de linea
                    palabra += letra

automata(cadena)
print("----------------------------------------------------------------------------------------------------------------")
print(f"SIMBOLOS : {tk_Simbolos}")
print(f"BOOLEAN : {tk_Boolean}")
print(f"CADENA : {tk_Cadena}")
print(f"NUMERO : {tk_Numero}")
print(f"ATRIBUTO : {tk_Atributo}")
