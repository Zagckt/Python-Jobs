# -*- coding: utf-8 -*-
"""27/10/2021.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x5NXsRuPk6Rh3GjXjXf_T9EPdgdH2Xvu
"""

LISTA=['sociales','Español','Matematicas','Ingles','Biologia','Etica y valores','Religion','Artistica','Tecnologia','fisica','ed,fisica',]
SUMA=0
for i in LISTA :
  print('ingrese la nota de ', i)
  NOTA=float(input())
  SUMA+=NOTA
print('El promedio es: ',SUMA/len(LISTA))

while True:
  num=int(input('ingrese un numero par: '))
  if num%2==0:
    break

while True:
  a=input('ingrese la palabra secreta :')
  a=a.lower()
  if (a=='abracadabra'):
    break