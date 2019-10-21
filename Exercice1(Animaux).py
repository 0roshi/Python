#!/usr/bin/env python
import random
noms = ['Arthur', 'Quentin','Theo','Vincent','Jeremy','Paulin','Alexys','Florent']
animo = ["l'ours","le loup","l'ornithorynque","la belette","la galinette cendree","le lombric"]
nom = random.randint(0,len(noms)-1)
anima = random.randint(0,len(animo)-1)
print(noms[nom]+" "+animo[anima]) 
