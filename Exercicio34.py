# -*- coding: utf-8 -*-
"""Exercicio34.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JqfqI-aAyQlFx5t1TDy4wD9LJ2WXzOdk
"""

sal = str(input('Digite o valor de seu salário: R$')).strip()
sal2 = float(sal)
if sal2 > 1250:
    print('Seu salário será reajustado para R${:.2f}.' .format(sal2 * 1.1))
else: 
    print('Seu salário será reajustado para R${:.2f}.' .format(sal2 * 1.15))