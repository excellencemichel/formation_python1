#coding:utf-8


"""
    En python les opérateur possibles sont
        + (addition)
        - (soustration)
        * (multiplication)
        / (division)

        %( modulo ->reste d'une division entière autrement dit division Euclidienne)

"""

division = 5 / 2

print(division)

entiere = int(division) #Ceci prend la partie avant la virgule
virgule= float(division)#Récupère tout et la partie entière et la virgule

derriere = 5%2 #Stocke le reste de la division 5/2



print("Juste la partie avant la virgule de 5 / 2: ", entiere)

print("Tout de résultat de 5/2 :" ,virgule)

print("Le modulo de 5 / 2 est:", derriere)


"""
    En python la priorité dans les opération sont les mêmes que
    les opérations en mathématique
    * prioritaire sur + et -
    () prioritaire sur tout
"""

resultat = 12 + 3 * 7 # Va d'abord faire 7*3 et ajouter le résultat à 12
print("Le resultat est :", resultat)