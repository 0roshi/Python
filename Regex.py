#!/usr/bin/env python 
# 
# 
#		Ici, le but est d'utiliser une RegEx afin de valider que la phrase
#		est au bon format, et d'afficher ses groupes. Une phrase étant valide si
#		tous ses mots commencent par une majuscule ou un chiffre, et les groupes 
#		sont composés d'un chiffre et du mot qui suit. 
#
#
phrase = input()
import re
match = re.search('^[a-z]\w*', phrase)
groupes = str(re.findall('[0-9]+ \w*', phrase))
result = "La phrase est au bon format. Les groupes sont {0}".format(groupes)
if match == None:
	if groupes != "[]":
		print(result)
	else:
		print("La phrase est au bon format. Pas de groupe")
else:
	print("La phrase n'est pas au bon format")
#simple verif
#print(match)

#match.groups() 

#2 regex: une regex format et une regex groupes
#obtenir les 4 bras: r'[0-9]+ \w*'
#définir le groupe: ([0-9]+ \w*)
# Pour la première lettre etant une majuscule r'[A-Z0-9]\w*

