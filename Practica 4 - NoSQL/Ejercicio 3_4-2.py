#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from psycopg2 import Error
import psycopg2
from geopandas import GeoSeries, GeoDataFrame
import pymongo as mongo

#Creacion del mapa vacio
world = GeoDataFrame.from_file('ne_10m_admin_0_countries.shp')

#Conexion con la base de datos de mongo
myClient = mongo.MongoClient("mongodb://localhost:27017/")
myTest = myClient["test"]
myTweets = myTest["tweets"]

#Guardar los datos en el mapa
i = 0
for location in myTweets.aggregate([{"$group":{"_id":{"codigo":"$codigo","pais":"$pais"},"population":{"$sum":1}}},{ "$sort": {"population": -1}}]):
	codigoWorld = location.get('_id').get('codigo')
	paisWorld = location.get('_id').get('pais')
	populationWorld = location.get('population')

	world.loc[world['NAME'] == paisWorld, 'population'] = populationWorld
	world.loc[world['SOV_A3'] == codigoWorld, 'population'] = populationWorld
	world.loc[world['SOV_A3'] == codigoWorld, 'escala'] = i
	world.loc[world['NAME'] == paisWorld, 'escala'] = i
	i = i + 1

#Configurar caracteristicas del mapa
world.plot(column='escala', cmap='Greens_r', alpha=1, categorical=False, legend=False, ax=None)

#Mostrar el mapa
plt.show()
