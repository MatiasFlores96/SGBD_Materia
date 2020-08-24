#!usr/bin/python3

from pandas import Series, DataFrame
import pandas as pd

"""
Calcular el valor medio de los deptos 2 ambientes en Capital Federal
"""

df = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')
 
df1 = df[(df['state_name'] == 'Capital Federal') & (df['property_type'] == 'apartment') & (df['rooms'] == 2)]
df1 = df1[df1.price_aprox_usd.notnull()]
print(df1['price_aprox_usd'])

#cantidadDepts = len(df1['price_aprox_usd'])
#precioTotal = df1['price_aprox_usd'].sum()

df2 = df1['price_aprox_usd']
print("Valor medio de los deptos de 2 ambientes en Capital Federal: ")
#print("$",precioTotal/cantidadDepts)
print(df2.mean(skipna=True))
