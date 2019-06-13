# -*- coding: utf-8 -*-

def r(x, y):
    return 9*x*x + y*y

def b(x, y):
    return 2*x*x + 25*y*y

def c(x, y):
    return -100*x + y*y*y

n = int(input())
for i in range(n):
    aux = input()
    aux = aux.split(" ")
    x = int(aux[0])
    y = int(aux[1])

    if r(x, y) > b(x, y) and r(x, y) > c(x, y):
        print('Rafael ganhou')
    if b(x, y) > r(x, y) and b(x, y) > c(x, y):
        print('Beto ganhou')
    if c(x, y) > b(x, y) and c(x, y) > r(x, y):
        print('Carlos ganhou')