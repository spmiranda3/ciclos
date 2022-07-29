from random import*
c = 0
while True:
    dado = randint(1, 6)
    print("Resultado del dado: ", dado)
    c += 1
    if dado == 3:
        print("numero suerte  3, al intento", c+1)
        break
