'''
    Cuenta y suma numeros enteros

'''

def contando_y_sumando():
    '''
        Entrada: no hay
        Salida : no hay, pero permite que el usuario capture numeros enteros y los cuenta y acumula hasta
                 que la suma es igual o superior a 1000
    '''

    fin = False
    contador = 0
    acumulador = 0

    while not fin:
        numero = int(input("Numero:"))

        contador = contador + 1
        acumulador = acumulador + numero 

        if acumulador >= 1000:
            fin = True

    print(f"suma = {acumulador}")
    print(f"cantidad de numeros = {contador}")

def main():
    '''
        Funcion principal
    '''

    #escribe tu código abajo de esta línea
    contando_y_sumando()

if __name__=='__main__':
    main()
