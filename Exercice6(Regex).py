#!/usr/bin/env python 
# 
# 
#
#

phrase = input()
import re
match = re.search(r'^[A-Z0-9][a-z]\w*', phrase)
all_ma = re.findall('[0-9]+ \w*', phrase)
result = "La phrase est au bon format. Les groupes sont {0}".format(all_ma)
if match == " ":
	print(result)
else:
	print("La phrase n'est pas au bon format")

#match.groups() 

#2 regex: une regex format et une regex groupes
#obtenir les 4 bras: r'[0-9]+ \w*'
#définir le groupe: ([0-9]+ \w*)
# Pour la première lettre etant une majuscule r'[A-Z0-9]\w*

