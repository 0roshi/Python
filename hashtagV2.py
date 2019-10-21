#!/usr/bin/env python
#exemple raté, affiche entre 2 hastags et une ligne après l'autre
#chaine = "adroit#a3#vroom#b52#colorant#e111"
#test = 1
#for i in chaine:
#	if i == "#":
#		if test == 1:
#			test = 2
#		else:
#			test = 1
#			print(";")
#	elif test == 2:
#		print(i)
#	else:
#		continue
digo = "0123456789"
chaine = "adroit#a3#vroom#b52#colorant#e111"
final = list("") # on initie juste en s'assurant que final est une list
# on va séparer la chaine de base, i devenant chaque chaine entre "#"
for i in chaine.split("#"):
# ensuite, on vérifie que la chaine se finit par un chiffre
	if i[-1] in digo:
#là on ajoute ensuite le résultat à un tableau, s'il se finit par un chiffre. 
		final.append(i)
#sinon, on passe à la chaine suivante
	else:
		continue
#essai raté de changement de string 
#mot = str(final)
#a = len(final)-1
#print(final[0], sep=";")
# 
#on définit "sep", le séparateur qui va venir entre chaque caractère du tableau
sep = ";"
# on "fusionne" sep avec le tableau: sep deviens le tableau accompagné du séparateur, sous format string
sep = sep.join(final)
# on affiche ensuite la nouvelle valeur
print(sep)
