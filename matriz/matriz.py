import numpy as np
import random


# genero la matriz  5 x 5
matriz = np.arange(1, 26).reshape(5, 5)
# recorro la matriz y cambio por numeros aleatorios 
for f in range(5):
    for c in range(5):
        matriz[f][c] = random.randint(1,10)

#///////////////////



print(matriz)
""" 
el primer for solamente itera cambiando el numero de indice de las filas [f] 
el segundo for itera cambiando el numero de indice de las columnas [c] 
si encuentra 2 numeros consecutivos, comprueba cual es mayor y compara con los siguientes 2
que deberian ser correlativos de manera ascendente o descendente segun el caso  """


# itera horizontalmente 
for f in range(5):
    for c in range(2):
        if (matriz[f, c] - matriz[f, c+1] == -1) or (matriz[f, c] -matriz[f, c+1]  == 1):
            if matriz[f, c] > matriz[f, c+1]:
                if (matriz[f, c+1] - matriz[f, c+2] == 1) and (matriz[f, c+2] - matriz[f, c+3] == 1):
                    print("encontrado")  # descendente
 
                    print(f"comienza en la fila {f} columna {c} y termina en fila {f} columna {c+3} ...")
                else:
                    pass
            else: 
                if (matriz[f, c+1] - matriz[f, c+2] == -1) and (matriz[f, c+2] - matriz[f, c+3] == -1):
                    print("encontrado")  # ascendente
                    print(f"comienza en la fila {f} columna {c} y termina en fila {f} columna {c+3} ...")
        

"""
este for hace practicamente lo mismo que el anterior pero de manera vertical  
El primero itera por las columnas y el segundo por las filas """

# itera verticalmente             
for c in range(5):
    for f in range(2):
        if (matriz[f, c] - matriz[f+1, c] == -1) or (matriz[f, c] -matriz[f+1, c]  == 1):
            if matriz[f, c] > matriz[f+1, c]:
                    if (matriz[f+1, c] - matriz[f+2, c] == 1) and (matriz[f+2, c] - matriz[f+3, c] == 1):
                        print("encontrado")  # descendente 
                        print(f"comienza en la fila {f} columna {c} y termina en fila {f+3} columna {c} ...")
                    else:
                        pass
            else:
                if (matriz[f+1, c] - matriz[f+2, c] == -1) and (matriz[f+2, c] - matriz[f+3, c] == -1):
                    print("encontrado")  #  ascendente
                    print(f"comienza en la fila {f} columna {c} y termina en fila {f+3} columna {c} ...")
   

           