# -*- coding: utf-8 -*-

def fat(n):
    if n == 0 or n == 1:
        return 1
    return n * fat(n-1)

x = int(input())
fat = fat(x)
print('{}'.format(fat))
