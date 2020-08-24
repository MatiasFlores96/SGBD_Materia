#!/usr/bin/python3

import re

str = "azul?, [rojo]. and'r' black {blue}. negro-'r'skkjlkjlk'"
print(str)

str = re.sub(r'[^a-z0-9\s]','',str)
print(str)


