# -*- coding: utf-8 -*-

nome = input()
sal_fixo  = float(input())
vendas = float(input())

print('TOTAL = R$ {:.2f}'.format(sal_fixo + vendas*0.15))