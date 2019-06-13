# -*- coding: utf-8 -*-

def fat(n):
    if n == 0 or n == 1:
        return 1
    return n * fat(n-1)

while 1:
    try:
        x, y = map(int, input().split())
        somaF = fat(x) + fat(y)
        print('{}'.format(somaF), end='\n')
    except EOFError:
            break
    
     