#!/usr/bin/env python
print("Saisissez l'année, vous saurez si elle est bissextile ou non.")
annee = int(input())
#on vérifie que l'année est divisible par 4 et pas par 100, ou par 400
if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
	print("L'année est bissextile.")
#essai (raté) de valeur invalide, mais python ne laisse pas cela se faire à cause du int() pour annee
#elif type(annee) != int :
#	print("La valeur est invalide.")
else:
	print( "L'année n'est pas bissextile.")

