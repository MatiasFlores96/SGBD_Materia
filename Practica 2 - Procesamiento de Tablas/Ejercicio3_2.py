#!usr/bin/python3

from pandas import Series, DataFrame
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.show()

3.2)

1) La ciudad con mayor costo de vida es Buenos Aires, por que la caja se encuentra mas arriba de las otras en
el grafico

2) La ciudad mas equitativa es La Plata, por que el valor de la mediana se encuentra en el centro de la caja

3) Pueden ser incorrectos los argumentos anteriores, debido a que el analisis de dicho grafico puede fallar, 
por que los precios dependen de los la distribucion de los barrios. Segun la localizacion, hay departamentos 
que pueden valer mas caros que otros, por lo cual el valor de la mediana en las cajas se vera afectado por ello.
Tambien influye en que el analisis previo no sea correcto, debido a que nosotros limitamos el valor maximo de 
precio, ya que sino se encontraban muchos outliers.
