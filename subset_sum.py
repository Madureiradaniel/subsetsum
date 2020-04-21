"""
Alogoritmos subset sum
"""

import time
import sys
import numpy as np
import os

"""dinâmica"""
def dinamico(lista, TAM, soma):
    
    #criacao da matriz com numpy
    matriz = np.zeros((TAM + 1 , soma + 1 ), dtype=int)

    # preenchendo matriz     
    for i in range(1, TAM + 1):
        for j in range(1, soma + 1):
            
            #verifico se o peso que eu tenho cabe na mochila
            if lista[i-1] <= j:
               matriz[i][j] = matriz[i-1][j - lista[i-1]] + (i) #valor do item 
            else:
                matriz[i][j] = matriz[i-1][j]

    #pegando o conjunto
    conjunto = []
    soma_aux =soma
    while True:        
        if TAM == -1:
            break;
        
        valor = matriz[TAM][soma]
                
        if valor == matriz[TAM - 1][soma]:
            TAM = TAM - 1
        else:
            TAM = TAM - 1
            conjunto.append(lista[TAM])
            soma =  soma - lista[TAM]
    

    if np.sum(conjunto) == soma_aux:              
        print("CONJUNTO ACHADO: ", conjunto)
        return True
    else:
        return False    
                         

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
lista = [3, 34, 6, 12, 5, 2]
lista.sort()
soma = int(sys.argv[1])
TAM = len(lista)


print("---------IMPLEMENTACAO DINAMICA------")
if dinamico(lista, TAM, soma):
    print("Existe um subconjunto DINAMICO")
else:
    print("nao existe um subconjunto!!")

print("\n----------RECURSIVO----------------")
if recursivo(lista, TAM, soma) : 
    print("Existe um subconjunto")
else:
    print("nao existe um subconjunto!!")
#backtracking()