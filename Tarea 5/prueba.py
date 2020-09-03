letras = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z')
numeros = (1,2,3,4,5,6,7,8,9,0)

def esLetra(letra):
    prueba = letra.lo
    for caracter in letras:
        if letra == caracter:
            return True

    return False

def esNumero(numero):
    for digito in numeros:
        if numero == digito:
            return True
        else:
            return False

cadena = "D"
cadena = cadena.lower()

print(esLetra(cadena))

