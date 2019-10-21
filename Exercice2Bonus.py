#!/usr/bin/env python
#
# Petit bonus: après avoir fait l'exercice sur les années bissextiles, j'ai voulu en faire une version qui donnait toutes 
#les années bissextiles de -3000 à 2020
#
#print("Saisissez l'année, vous saurez si elle est bissextile ou non.")
#annee = int(input())
#on vérifie que l'année est divisible par 4 et pas par 100, ou par 400
for i in range(5021):
	if (i-3000) % 4 == 0 and (i-3000) % 100 != 0 or (i-3000) % 400 == 0:
		o=str(i-3000)
		print(o + " est bissextile") 
#essai (raté) de valeur invalide, mais python ne laisse pas cela se faire à cause du int() pour annee
#elif type(annee) != int :
#	print("La valeur est invalide.")
	else:
		continue
#	print( "L'année n'est pas bissextile.")

