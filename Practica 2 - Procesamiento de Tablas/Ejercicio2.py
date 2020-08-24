#!usr/bin/python3

from pandas import Series, DataFrame
import pandas as pd
from matplotlib import pyplot as plt

"""
Para aquellas propiedades de Capital Federal que tengan informacion geograﬁca
se pide escribir un programa para hacer un scatterplot de las propiedades que
diﬁeran a lo sumo en 0.05 grados en latitud y longitud respecto al centro
geograﬁco de la ciudad. Obs.: obtener las coordenadas del centro de la ciudad
de modo aproximado con googlemaps).
"""

df = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

df1 = df[(df['state_name'] == 'Capital Federal')]
df1 = df1[df1.lat.notnull() & df1.lon.notnull()]

df2 = DataFrame(df1, columns=['lat', 'lon'])
print(df2)

#Filtro
latCentroC = -34.617008
lonCentroC = -58.445095

df2 = df2[(df2['lat'] <= latCentroC + 0.05) & (df2['lat'] >= latCentroC - 0.05)]
df2 = df2[(df2['lon'] <= lonCentroC + 0.05) & (df2['lon'] >= lonCentroC - 0.05)]

df2.plot.scatter(x='lon', y='lat');

plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.title("PROPIEDADES CAPITAL FEDERAL")
plt.show()
