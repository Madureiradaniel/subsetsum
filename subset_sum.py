"""
Alogoritmos subset sum
"""

import time
import numpy as np

"""dinâmica"""
def dinamico():
    ...

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



#dinamico()

print("RECURSIVO")
if recursivo(lista, TAM, soma) : 
    print("Existe um subconjunto")
else:
    print("nao existe nenhum subconjunto para esta soma")
#backtracking()


matriz = np.array([(1,2,3),(3,2,1)])