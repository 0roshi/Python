#!/usr/bin/env python

#
# le but ici est de faire un programme qui va renvoyer le nombre de voyelles dans une phrase
# saisie par l'utilisateur à l'aide d'une fonction
#
#
# On commence par définir un dictionnaire contenant nos voyelles (pour éviter que 0 ne soit 
# considéré comme une string, on évite les "")
dic = { "a":0,"e":0,"i":0,"o":0,"u":0,"y":0 }
# On demande à l'utilisateur de rentrer une phrase
phrase = input()
# On vérifie ensuite chaque si chaque lettre est une voyelle (donc contenue dans le dictionnaire)
# Ici, nos voyelles sont des clés. On vérifie donc via dic.key pour comparer la lettre aux voyelles
for z in phrase:
	if z in dic.keys():
# Si la lettre est présente (donc voyelle), il incrémente la valeur de la voyelle correspondante
		dic[z] = dic[z]+1
	else:
# Si la lettre n'est pas une voyele, il passe
		continue
# Pour conclure, on affiche le compte 
print(dic)
