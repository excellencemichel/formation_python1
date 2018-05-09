#coding:utf-8

"""
Les fonctions lambda
le fait de faire juste 'lambda:print("Faire quelque chose")'
équivaut écrire un fonction sans nom, comme :
        def :
            print("Fait ça")
    et cela ne fonctionne pas

Pour remedier à celà il faut alors stocker la valeur de
retour de la fonction anonyme lambda dans une variable
Cette variable peut être appélée comme une fonction à part
entière pour retouner la valeur de retour de la fonction
anonyme lambda
lambda est un racoursi de création de fonction
Elle peut prendre autant de parametre qu'on désir et faire
des traitement qu'on désir
l'appel de la variable stockant le résultat de la fonction
lambda peut faire tout ce qu'une fonction ordinare peut faire
à savoir le nommage des argument pour faire l'ordre etc...


"""


leBj = lambda : print("Bonjour !") #Stockage de la valeur de retour de la fonction lambda
#Ici la fonction lambda ne prend pas de parametres

leBj()#Appel de la variable sous forme de fonction,
#puisque la fonction anonyme lambda ne prend pas de parametre
#donc l'appel aussi ne prend pas d'argument



TTC = lambda prixHT: prixHT + (prixHT * 20/100 ) #Ici la fonction anonyme lambda
#Prend de parametre donc l'appel doit fournir ces parametres sous forme d'arguments

resultat = TTC(24)

print(resultat)

print(TTC(2500))



print("Après la fonction lambda...")


nom_Complet = lambda nom, prenom: print("Ton nom complet est {} {} ".format(nom, prenom))

nom_Complet(prenom="Pépé", nom="Michel")

import math

racine = lambda x: print(math.sqrt(x))

racine(25)

somme = lambda a, b : print(a+b)

somme(7,12)