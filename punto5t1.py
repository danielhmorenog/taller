def main():
    stocks = {
    '''Se define un diccionario con los valores que 
    encontramos dentro de las siguientes llaves
    debemos recordar que la estructura de los diccionarios
    esta definida por una llave y un valor que se hace separadas
    por comas'''
        'IBM': 146.48,
        'MSFT':44.11,
        'CSCO':25.54
    }
    
    #print out all the keys
    for c in stocks:
    '''en este caso vemos que con una funcion for recorremos el
    diccionario para imprimir exclusivamente las llaves de cada
    elemento'''
        print(c)
    
    #print key and values
    for k, v in stocks.items():
    '''en este caso vemos que a diferncia de lo anterior se imprimen
    las llaves y los valores correspondientes a cada llave'''
        print("Code : {0}, Value : {1}".format(k, v))

if __name__ == '__main__':
''' en este caso le estados diciendo a python que este archivo funciona
bien sea llamado por él mismo o desde otro archivho'''
    main()
    
'''este es el desarrollo del punto 5 taller 1'''