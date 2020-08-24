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

#Creacion del campo codigo  
myTweets.update_many({},{"$set" : {"codigo":"null"}}) 
myTweets.update_many({},{"$set" : {"pais":"null"}}) 



try:
	#Conexion con postgres
	con = psycopg2.connect(database = 'world', user = 'postgres', host = 'localhost', password = '120396')
	cursor = con.cursor()
	
	#Almacenamiento de los datos de las tablas de world en variables
	countryTable = "select name, code, localname, population from country order by population;"	
	cursor.execute(countryTable)
	country = cursor.fetchall()
	
	cityTable = "select city.name, city.countrycode, country.name from city inner join country on city.countrycode = country.code;"
	cursor.execute(cityTable)
	city = cursor.fetchall()
	
	for location in myTweets.find({},{"user.location":1, "codigo":1, "_id":0}):
		codigo = " "
		pais = " "
		estado = False
		localizacion = location.get('user').get('location')

		if(localizacion != None):
			if ('NY' in localizacion or 'U.S.A' in localizacion or 'Arizona' in localizacion  or 'TX' in localizacion or 'Florida' in localizacion or 'Texas' in localizacion):
				estado = True
				codigo = 'USA'
				pais = 'United States'
			elif ('CABA' in localizacion or 'Buenos Aire' in localizacion or 'BS.AS' in localizacion):
				estado = True
				codigo = 'ARG'
				pais = 'Argentina'
			elif (estado == False):
				for row in country:		
					if (row[0] in localizacion and estado == False):
						estado = True
						codigo = row[1]
						pais = row[0]
						break
					elif (row[1] in localizacion and estado == False):
						estado = True
						codigo = row[1]
						pais = row[0]
						break
					elif (row[2] in localizacion and estado == False):
						estado = True
						codigo = row[1]
						pais = row[0]
						break
						
				if (estado == False):
					for fila in city:		
						if (fila[0] in localizacion):
							estado = True
							codigo = fila[1]
							pais = fila[2]

		valores = { "$set": { "codigo": codigo, "pais": pais } }
		myTweets.update_many({"user.location" : localizacion}, valores)

	for location in myTweets.find({},{"user.location":1, "codigo":1, "pais":1, "_id":0}):
		print (location)

#Excepcion de error
except (Exception, psycopg2.Error) as error:
    print ("Error al cargar los datos", error)
finally:
	# cerrando conexion con la base de datos
	if (con):
		cursor.close()
		con.close()
