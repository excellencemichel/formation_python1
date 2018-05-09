#La mathématique
import math
from fractions import Fraction #Module pour les fractions
import random #Module pour gérer les aleatoir

"""
Le module 'math'
   Le module math contient des fonction mathématiques
     Quelques fonctions usuelles
       'pow(x,)': Elève x à la puissance y

       'sqrt(param)' : Donne la racine du paramètre

       'exp(param) : Donne l'exponentielle du paramètre

       'fabs(param): Donne la valeur absolu du parametre
    Le resultat de ces fonctions est nombre flotant

       'ceil(param)': Arondi le parametre à l'entier suivant
       'floor(param' : Arondi le paramètre à l'entier précedent
       'trunc(param)' : Envoi le paramètre tel qu'elle sans arondire


Les aleatoir:
  Le module 'random' permet de gérer les aléatoirs:
    Pour les nombres
     'randrange(x,y,z): Permet de ranvoyer un nombre entre :
         x: Borne inferieur(non incluse)et
         y: Borne superieur (incluse)
         z :Par défaut égale à 1, l'écart entre les nombre qui doivent générés
          Voici l'intervalle : ]x,y]
           Si randrange(10,20,2) :Seulement : 12,14,16,18,20 pouront être
           généré aléatoirement(si on ne met pas 2, lesnombre de 11 à 20
           êtregénés aléatoirement)

     'randint(x,y):Générer des nombres aléatoir entre:
        x: Borne inférieur compreise et
        y : Borne superieure comprise aussi
         Voici l'intervalle : [x,y]
         Soit le fonctionnement des dés randint(1,6): Des nombres aléatoirs de
         1 à 6


    Pour les séquences :
       La fonction 'choice' permet de générer un élément aléatoir entre les éléments
       d'une séquence(conteneur)

       La fonction 'shuffle' permet de mélanger les éléments d'une séquences sans
       rien retourner juste melanger les élément des objet conteneurs
       


"""

print(math.sqrt(49)) #La racine carrée de 49 =>7
print(math.fabs(-3))#La valeu absolue de -3 => 3
print(math.pow(12,2)) #Elève 12 à la puissance 2, (un nbre flotant)
print(12**2) #Donne un nombre un nombre nom flotant


#Utilisation des alaetoirs
#Aleatoir des nombres



