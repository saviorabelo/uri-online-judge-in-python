# -*- coding: utf-8 -*-

lista = [0,1,1]

r = "0,1,1"
ant = 1
atual = 1
valor = int(input())

for _ in range(valor-3):
    aux = atual
    atual += ant
    ant = aux
    lista.append(atual)
    
print(str(lista[0:valor]).replace(",","").replace("[","").replace("]",""))
