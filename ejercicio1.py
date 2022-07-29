
def numero():
    lista = []
    numeros = 0
    contador = 0
    Total = 0
    import sys
    print("digita unnumero.")
    numeroa = int(sys.stdin.readline())
    while numeroa != 0:
        contador += 1
        lista.append(numeroa)
        print("digita otro numero:")
        numeroa = int(sys.stdin.readline())
        Total = sum(lista)
        numeros = (Total/contador)
    else:
        print("Elpromedio de los numeros ingresado es", numeros)


numero()
