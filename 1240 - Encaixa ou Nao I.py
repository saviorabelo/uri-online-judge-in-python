# -*- coding: utf-8 -*-

def encaixa(a,b):
    if len(a) < len(b):
        return False
    elif len(a) == len(b):
        if a==b:
            return True
        else:
            return False
    else:
        x = len(b)
        y = len(a)
        if a[-x:y] == b:
            return True
        else:
            return False

n = int(input())
for i in range(n):
    aux = input()
    aux = aux.split(" ")
    a = str(aux[0])
    b = str(aux[1])

    if encaixa(a,b):
        print('encaixa')
    else:
        print('nao encaixa')