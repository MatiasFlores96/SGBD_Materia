#!/usr/bin/python3

import re
import collections
import random
from matplotlib import pyplot as plt

#Procesar el archivo king_lear.txt
archivo = open('king_lear.txt','r')
str = archivo.read()
archivo.close()

print('Achivo king_lear.txt')
#print(str)

#Pasar las palabras a minuscula
str = str.lower()

print('\nPalabras en minuscula')
#print(str)

#Descartar los signos de puntuacion
str = re.sub(r'[^a-z0-9\s]','',str)

print('\nSin signos de puntuacion')
#print(str)

#Descartar palabras prohibidas
archivoProhibido = open('palabrasProhibidas.txt','r')
strProhibido = archivoProhibido.read()
archivoProhibido.close()

palabrasProhibidas = re.split(r'\W+',strProhibido)

#print(palabrasProhibidas)

for palabraProhibida in palabrasProhibidas:
	str = re.sub('\s' + palabraProhibida + '\s',' ', str)

print('\nSin palabras prohibidas')
#print(str)

#Separar y contar las ocurrencias de las palabras
def convert(string):
    li = re.split(r'\W+',string)
    return li
  
cnt = collections.Counter()
for word in convert(str):
     cnt[word] += 1

print('\nSeparar y contar las ocurrencias de las palabras')
#print(list(cnt))

#Ordenar de modo decendente las palabras por cantidad de ocurrencia
print('\nOrdenado de modo decendente por cantidad de ocurrencia')
#print(cnt)

#Respuestas
print('\nRespuestas:')
print('¿Cuantas palabras tiene el texto?')
print(len(cnt))

print('\n¿Cauales son las 5 palabras mas usadas?')
print(cnt.most_common(5))

#Histograma de las 10 palabras mas usadas
cntDiez = cnt.most_common(10)
strDiez = []
numDiez = []

for elem in cntDiez:                  
    strDiez.append(elem[0])
    numDiez.append(elem[1])

xs  = [i + 0.5 for i, _	in enumerate(strDiez)]

plt.bar(xs, numDiez)
plt.xlabel("Palabras")
plt.ylabel("# Ocurrencias")
plt.title("10 PALABRAS MAS USADAS")
plt.xticks([i +	0.5 for	i, _ in	enumerate(strDiez)], strDiez)
plt.show()
