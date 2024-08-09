def divisores(numero):
    c = 1
    n = 0
    while c < numero:
        if numero % c == 0:
            n = n+c
        c= c+1
    return n




def main():
    #escribe tu código abajo de esta línea
    numero = int(input("Dame un número entero positivo: "))


    if numero == divisores(numero):
        print("Es perfecto")
    else:
        print("No es perfecto")
    



if __name__=='__main__':
    main()
