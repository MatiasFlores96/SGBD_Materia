#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from psycopg2 import Error
import psycopg2
from geopandas import GeoSeries, GeoDataFrame

world = GeoDataFrame.from_file('ne_10m_admin_0_countries.shp')

try:
	con = psycopg2.connect(database = 'world', user = 'postgres', host = 'localhost', password = '2525')

	cursor = con.cursor()
	postgreSQL_select_Query = "select name, code, population from country order by population"
	cursor.execute(postgreSQL_select_Query)
	mobile_records = cursor.fetchall()
	i = 0
	for row in mobile_records:		
		world.loc[world['NAME'] == row[0], 'population'] = row[2]
		world.loc[world['SOV_A3'] == row[1], 'population'] = row[2]
		world.loc[world['SOV_A3'] == row[1], 'escala'] = i
		world.loc[world['NAME'] == row[0], 'escala'] = i
		i = i + 1

except (Exception, psycopg2.Error) as error:
    print ("Error al cargar los datos", error)
finally:
	# closing database connection
	if (con):
		cursor.close()
		con.close()

world.plot(column='escala', colormap='Purples', alpha=1, categorical=False, legend=False, axes=None)

plt.show()
