'''
Muestra los numeros pares entre a y b
'''

def muestra_pares(a,b):
    '''
        Entrada: Valor inferior (a), Valor superior (b)
        Salida : No hay, pero se muestra en consola los valores par entre a y b
    '''
    c = a

    while c <= b:
        if c % 2 == 0:
            print(c)

        c=c+1

def main():
    '''
        Función principal

    '''
    #escribe tu código abajo de esta línea
    a=int(input("Valor inferior:"))
    b=int(input("Valor superior:"))

    muestra_pares(a,b)


if __name__=='__main__':
    main()
