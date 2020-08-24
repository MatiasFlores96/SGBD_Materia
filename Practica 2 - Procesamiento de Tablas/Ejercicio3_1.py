#!usr/bin/python3

from pandas import Series, DataFrame
import pandas as pd
from matplotlib import pyplot as plt

"""
Considerando solamente los deptos. de 3 ambientes, escribir un programa que
graﬁque un boxplot de los precios de esos deptos. de las 5 ciudades mencionada
"""

df = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

#df1 = df[((df['state_name'] == 'Capital Federal')  | (df['place_name'] == 'Córdoba') | (df['place_name'] == 'Rosario') | (df['place_name'] == 'La Plata') | (df['place_name'] == 'Mar del Plata')) & (df['property_type'] == 'apartment') & (df['rooms'] == 3)]

df1 = df[((df['state_name'] == 'Capital Federal')  | (df['place_name'] == 'Córdoba') | (df['place_name'] == 'Rosario') | (df['place_name'] == 'La Plata') | (df['place_name'] == 'Mar del Plata')) & (df['property_type'] == 'apartment') & (df['rooms'] == 3) & (df['price_aprox_usd'] < 1000000)]

df1 = df1[df1.price_aprox_usd.notnull()]

df1.loc[df1['state_name'] == 'Capital Federal', 'place_name' ] = 'Buenos Aires'

df2 = DataFrame(df1, columns=['place_name', 'price_aprox_usd'])

print(df2)

df2.boxplot(column = ['price_aprox_usd'] , by = 'place_name')

plt.title("PRECIOS")
plt.show()


