cadena1 = '00000101000' #Correcta
cadena2 = '00011011000' #incorrecta

def AFD(entrada):
    estado = 0

    for letra in range(len(entrada)):
        if estado == 0:
            if entrada[letra] == '1':
                estado = 1
            elif entrada[letra] == '0':
                estado = 0
            else:
                print("Error, cadena incorrecta")
                return
        elif estado == 1:
            if entrada[letra] == '0':
                estado = 2
            else:
                print("Error, cadena incorrecta")
                return
        elif estado == 2:
            if entrada[letra] == '1':
                estado = 3
            else:
                print("Error, cadena incorrecta")
        elif estado == 3:
            if entrada[letra] == '0':
                estado = 3
            else:
                print("Error ,cade incorrecta")
                return

    print("Cadena aceptada :)")

AFD(cadena1)
AFD(cadena2)