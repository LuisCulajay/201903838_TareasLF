cadena1 = "__s1"
cadena2 = "3servidor"

letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z')
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

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
    cadena = cadena.lower()
    for letra in cadena:
        if estado == 0:
            if letra == "_":
                estado = 1
            elif esLetra(letra):
                estado = 2
            else:
                print(f"Error, cadena {cadena} invalida")
                return
        elif estado == 1:
            if letra == "_":
                estado = 1
            elif esLetra(letra):
                estado = 3
            else:
                print(f"Error, cadena {cadena} invalida")
                return
        elif estado == 2:
            if esLetra(letra):
                estado = 2
            elif esNumero(letra):
                estado = 4
            else:
                print(f"Error, cadena {cadena} invalida")
                return
        elif estado == 3:
            if esNumero(letra):
                estado = 4
            else:
                print(f"Error, cadena {cadena} invalida")
                return

    print(f"Cadena {cadena} aceptada")

automata(cadena1)
automata(cadena2)