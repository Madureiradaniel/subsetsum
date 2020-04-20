"""
Alogoritmos subset sum
"""

import time
import numpy as np

"""dinâmica"""
def dinamico(lista, TAM, soma):

    matriz = np.ones((TAM, TAM), dtype=np.int32)
    
    for i in range(TAM):
        matriz[i][0] = True

    for i in range(1, TAM ):
        matriz[0][i] = False

    for i in range(1, TAM):
        for j in range(1, TAM):
            if j < lista[i - 1]:
                matriz[i][j] = matriz[i-1][j]
            if j>= lista[i-1]:
                matriz[i][j] = (matriz[i - 1][j] or matriz[i-1][j - lista[i-1]])

    print(matriz[TAM][soma])

"""recursiva"""
def recursivo(lista, TAM, soma):

    # se a soma é zero
    if(soma == 0):
        return True
    
    #se o tamanho for zero , lista vazia
    if(TAM == 0 and soma !=0 ):
        return False

    if(lista[TAM - 1] > soma):
        return recursivo(lista, TAM - 1, soma)

    return recursivo(lista, TAM-1, soma) or recursivo(lista, TAM-1, soma-lista[TAM - 1])


"""backtracking"""
def backtracking():
    ...


"""EXECUCAO"""
lista = [3, 34, 4, 12, 5, 2]
soma = 19
TAM = len(lista)



dinamico(lista, TAM, soma)

print("RECURSIVO")
if recursivo(lista, TAM, soma) : 
    print("Existe um subconjunto")
else:
    print("nao existe nenhum subconjunto para esta soma")
#backtracking()