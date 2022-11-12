"""
Nombre: Simple
Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.
Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.
"""
import random

def gen_list():
    lista = []
    id = 1
    for i in range(0, 10):
        edad = random.randint(1, 100)
        diccionario = {'id':id, 'edad':edad}
        lista.append(diccionario)
        id += 1
    
    return lista


def sort():
    lista_ordenada = sorted(gen_list(), key = lambda i: -i['edad'])
    print(f"la persona de menor edad es: {lista_ordenada[9]['id']}")
    print(f"la persona de mayor edad es: {lista_ordenada[0]['id']}")
    
    return lista_ordenada
    



        
sort()