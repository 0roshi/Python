#!/usr/bin/env python3
#
#	Le but est de demander à l'utilisateur de rentrer un chiffre, et de renvoyer  "Nope" si l'utilisateur n'a pas rentré de chiffre.
#
#
def Erreur():
	print("Veuillez entrer un chiffre")
	entrée = input()
	try:
		chiffre = int(entrée)
		print("Voici votre chiffre multiplié par 3")
		mult = chiffre * 3
		print(mult)
		return OK

	except ValueError:
		print("NOPE!")
		return VErr

Erreur()
