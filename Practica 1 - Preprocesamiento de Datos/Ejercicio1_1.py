#!/usr/bin/python3

import re

S = input("Ingrese texto: ")

match = re.search(r'[^IVXLCDM]', S) #Matchea los valores que no se encuentran entre corchetes. El ^ indica todos

if match:
        print('FALSE')
else:
	print('TRUE')

