import csv

def registros():
    with open("RegistrosCSV.csv") as archivo:
        registros = csv.reader(archivo)

        NumeroRegistro = 0

        print("---------------------------------------------------------------------")
        print("                          REGISTROS CSV                              ")
        print("---------------------------------------------------------------------")

        for i in registros:
            NumeroRegistro += 1
            print(f"* Registro: {NumeroRegistro}")
            print(f"    Continente: {i[0]}")
            print(f"    País: {i[1]}")
            print(f"    Codigo de Área: {i[2]}")
            print(f"    Presidente: {i[3]}")

        print(f"Tipo de estructura de dato: {type(registros)}")