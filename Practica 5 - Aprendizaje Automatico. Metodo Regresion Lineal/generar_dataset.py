#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import statistics as stats

df = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

def sacarOutliers(df, barrio, rooms):
	df2 = pd.DataFrame()
	
	if ((df[(df['place_name'] == barrio) & (df['rooms'] == rooms)]).empty == False):
		df2 = df[(df['place_name'] == barrio) & (df['rooms'] == rooms)].copy()
		media = stats.median(df2['price_aprox_usd'])
		
		if(len(df2) < 2):
			desvio = int(df2['price_aprox_usd'])
		else:
			desvio = int(stats.stdev(df2['price_aprox_usd']))
			
		maxPrice = media + 3 * desvio
		minPrice= media - 3 * desvio 

		df2.loc[(df2.price_aprox_usd >= minPrice) & (df2.price_aprox_usd <= maxPrice), 'valido'] = True
		df2 = df2[df2.valido.notnull()]
						
	return df2
	
def estimarNivelSocioeconomico(df):
	rooms = 3
	df1 = df[(df['state_name'] == 'Capital Federal') & (df['property_type'] == 'apartment') & (df['rooms'] == rooms)]
	df1 = df1[df1.price_aprox_usd.notnull()]

	barrios = []

	for barrio in df1['place_name']:
		if barrio not in barrios:
			barrios.append(barrio)

	dfB = pd.DataFrame(columns = ['barrio', 'media'])
	
	val = Series(barrios)
	dfB['barrio'] = val

	for barrio in barrios:
		df2 = sacarOutliers(df1, barrio, rooms)

		media = stats.median(df2['price_aprox_usd'])
		
		dfB.loc[dfB['barrio'] == barrio, 'media'] = media

	dfB = dfB.sort_values(by='media', ascending=True)
	
	d = {}
	cont = 1
	for i, row in dfB.iterrows():
		d[row[0]] = cont
		cont += 1

	return d

df1 = df[(df['state_name'] == 'Capital Federal') & (df['property_type'] == 'apartment') & (df['rooms'] <= 8)]
df1 = df1[df1.place_name.notnull()]
df1 = df1[df1.rooms.notnull()]
df1 = df1[df1.surface_total_in_m2.notnull()]
df1 = df1[df1.price_aprox_usd.notnull()]

barrios = []

for barrio in df1['place_name']:
	if barrio not in barrios:
		barrios.append(barrio)

df3 = pd.DataFrame()

for barrio in barrios:
	for i in range(1, 9):
		if ((df[(df['place_name'] == barrio) & (df['rooms'] == i)]).empty == False):
			df2 = sacarOutliers(df1, barrio, i)

			df3 = pd.concat([df3, df2])

dicBarriosMedia = estimarNivelSocioeconomico(df)

print('ns,mc,ca,vp')

for i, row in df3.iterrows():
	if row.place_name in dicBarriosMedia:
		print(str(dicBarriosMedia[row.place_name])+',',str(row.surface_total_in_m2)+',',str(row.rooms)+',',row.price_aprox_usd)

