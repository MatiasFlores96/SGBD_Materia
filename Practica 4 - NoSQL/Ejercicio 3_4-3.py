#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import collections
import random
from matplotlib import pyplot as plt
import pymongo as mongo
from wordcloud import WordCloud, STOPWORDS

#Conexion con la base de datos de mongo
myClient = mongo.MongoClient("mongodb://localhost:27017/")
myTest = myClient["test"]
myTweets = myTest["tweets"]

archivoProhibido = open('nube.txt','r')
strProhibido = archivoProhibido.read()
archivoProhibido.close()
#Descartar palabras prohibidas
palabrasProhibidas = re.split(r'\W+',strProhibido)

def convert(string):
    li = re.split(r'\W+',string)
    return li


def obtenerTexto (pais):
	cnt = collections.Counter()

	for location in myTweets.find({"pais": pais},{"text": 1, "_id":0}):
		texto = location.get('text')
		#Pasar las palabras a minuscula
		tweet = texto.lower()
		if (":" in tweet):
			tweet = tweet.split(":", 1)[1]
		
		#Descartar los signos de puntuacion
		tweet = re.sub(r'[^a-z0-9\s]','',tweet)
		
		for palabraProhibida in palabrasProhibidas:
			tweet = re.sub('\s' + palabraProhibida + '\s',' ', tweet)
		
		#Separar y contar las ocurrencias de las palabras
		for word in convert(tweet):
			cnt[word] += 1
			
	data = cnt.most_common(20)
	return data


def text_size(total):
    return total

#Genera la nube de palabras que va a ser graficada
def generarNube(pais):
	data = obtenerTexto(pais)
	wordcloud = WordCloud(
			background_color='white',
			stopwords=STOPWORDS,
			max_words=20,
			max_font_size=40, 
			scale=3,
			random_state=1
		).generate(str(data))
	
	return wordcloud
	
#Grafica las dos nubes de palabras
def graficarNube(): 
	pais1 = "United States"
	pais2 = "United Kingdom"

	wordcloud1 = generarNube(pais1)
	wordcloud2 = generarNube(pais2)

	fig = plt.figure(1, figsize=(12, 12))
	fig.add_subplot(1,2,1)
	plt.imshow(wordcloud1)
	plt.title(pais1)
	plt.axis('off')

	fig.add_subplot(1,2,2)
	plt.imshow(wordcloud2)
	plt.title(pais2)
	plt.axis('off')

	plt.show()


graficarNube()
