#!usr/bin/python3

from pandas import Series, DataFrame
import pandas as pd
from matplotlib import pyplot as plt

"""
Hacer un graﬁco de barras por cantidad de ambientes en
Capital Federal quitando los outliers
"""

df = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')
 
df1 = df[(df['state_name'] == 'Capital Federal')]
df1 = df1[df1.rooms.notnull()]
df1 = df1['rooms']

print(df1.value_counts())
df2 = pd.DataFrame(df1.value_counts())

df2.plot.bar();

plt.xlabel("Ambientes")
plt.ylabel("# Departamentos")
plt.title("CANTIDAD AMBIENTES EN CAPITAL FEDERAL")
plt.show()

