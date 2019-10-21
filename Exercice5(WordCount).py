#!/usr/bin/env python
#
# On cherche cette fois à compter le nombre de mots et de lignes dans un fichier, pour l'exemple
# mon script Voyelles.py
#
# On importe une bibliothèque qui va nous permettre d'utiliser plusieurs séparateurs.
# Attention cependant, c'est senseible, et toutes les valeurs doivent être présentes.
# exemple: pour inclure un espace et un retour à la ligne, on met ' |\n'. si l'on met ' \n', 
# il ne recherchera que la combinaison de l'espace ET du retour à la ligne. 
import re
# ici on appelle un fichier "essai.txt", créé au préalable, avec le chemin sur la machine. 
# 
file = open('/home/formation/essai.txt','r')
# On affecte son contenu à la variable "fichié"
fichié = file.read()
# On ferme le fichier (on a plus besoin de le lire)
file.close
# Et on s'occupe de séparer chaque retour à la ligne et chaque espace, afin de délimiter nos "mots"
word = re.split(' |\n',fichié)
# Même chose, mais ici comme seul un séparateur est nécéssaire, on utilise juste split.
line = fichié.split("\n")
# On initialise deux variables
words = 0
lines = 0
# Et on incrémente pour chaque mot notre compte
for i in word :
	words = words + 1
for i in line : 
	lines = lines + 1
# On enlève 1, car il existe un retour à la ligne à la fin de chaque fichier. 
lines = lines - 1
words -= 1
# Ici, on formatte juste la phrase de façon à la rendre plus simple à lire et éditer via
# format. 
phrase = "le fichier comporte {lignes} lignes et {mots} mots.".format(
mots=words,
lignes=lines)
print(phrase)
