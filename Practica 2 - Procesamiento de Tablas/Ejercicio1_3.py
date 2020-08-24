#!usr/bin/python3

from pandas import Series, DataFrame
import pandas as pd
from matplotlib import pyplot as plt

"""
Hacer un graﬁco de barras horizontal de los 10 barrios con mayor
cantidad de publicaciones de deptos. de 2 ambientes en Capital Federal
"""

df = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')
 
df1 = df[(df['state_name'] == 'Capital Federal') & (df['property_type'] == 'apartment') & (df['rooms'] == 2)]
df1 = df1['place_name']

df2 = pd.DataFrame(df1.value_counts())
df2 = df2[:10]
print(df2)

df2.plot.barh();

plt.xlabel("# Departamentos de 2 ambientes")
plt.ylabel("Barrios")
plt.title("BARRIOS CAPITAL FEDERAL")
plt.show()
