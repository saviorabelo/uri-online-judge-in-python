# -*- coding: utf-8 -*-

def bissexto(n):
    bissexto = 0
    festival = 0
    if (n%4==0 and not n%100==0) or n%400==0:
        bissexto = 1
        print('This is leap year.')
    if n%15==0:
        festival = 1
        print('This is huluculu festival year.')
    if (bissexto) and (n%55==0):
        festival = 1
        print('This is bulukulu festival year.')
    if (not bissexto) and (not festival):
        print('This is an ordinary year.')

while 1:
    try:
        x = int(input())
        bissexto(x)
        print('')
    except EOFError:
            break