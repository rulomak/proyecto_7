import random

# funcion generadora 
""" creo una lista vacia, recorro un rango de 10, asigno un valor random a edad y creo un diccionario
con id y edad,  luego agrego el diccionario a la lista, retorno la lista.   """
def gen_list():
    lista = []
    for i in range(1, 11):
        edad = random.randint(1, 100)
        diccionario = {'id': i, 'edad':edad}
        lista.append(diccionario)
        
    
    return lista

# funcion ordenar 
""" creo una variable a la cual le asigno la funcion generadora que retorna la lista, ordeno con sorted()
 por la clave de edad de mayor a menor y muestro por consola id de menor y mayor edad, retorno lista ordenada """
def sort():
    lista_ordenada = sorted(gen_list(), key = lambda i: -i['edad'])
    print(f"la persona de menor edad es: {lista_ordenada[-1]['id']}")
    print(f"la persona de mayor edad es: {lista_ordenada[0]['id']}")  
    #print(lista_ordenada)
    return lista_ordenada
    


sort()
    


