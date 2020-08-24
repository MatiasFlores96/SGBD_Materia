#!/usr/bin/python3

import re

str = 'nombre1,apellido1,122112/nombre2,apellido2,2/nombreN,apellidoN,15/'

#findall y tuplas
tuplas = re.findall(r'([\w]+),([\w]+),([\d]+)/?', str)

for tuple in tuplas:
	print(tuple[1] + ' ' + tuple[0])
