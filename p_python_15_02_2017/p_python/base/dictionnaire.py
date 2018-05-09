#Dictionnaire
#Les dictionnaire se créés avec les accolades {}

"""
Les dictionnaire sont des objets comptenaires
à la diference des listes qui eux ordonne les éléments contenus, le 'dict'
ne met de l'ordre dans ses éléments
on accede  les éléments à travers les clés qui detiennet la key de la porte
tout passe par les keys

-Les dictionnaires avec les parametres de fonction
  si une fonction à nombre de parametre inconu d'avance, stock les parametre
  non nommés dans une liste(tuple), les parametre nommés eux sont stockés dans
  un dictionnaire ,
___________________________________
On peut également donner à une fonction un dictionnaire comme argument de
travaile, si la fonction prend des parametres nommés , on prend la clé de ces
fonctions en changeant leur valeur dans le dico
"""

#On peut créer initialemnt un dico comme ceci
dico = {"clé":"valeur", "a":1,"b":2}

#ou le créer vide après la remplir
dico1 ={}
dico1["val1"]="première valeur"

#Parcours des dico
dico1 ={"A":1,"B":2,"C":3,"D":4,"E":5}

for n in dico1: #Quand tente de parcourir un dico simplement avec 'for'
                #en réalité ce sont les clés qu'on parcours car c'est la clé
               # qui detient la porte
    print(n)

#-parcours explicite des clés
for n in dico1.keys():
    print(n)

#-parcours explicite des valeurs

for n in dico1.values():
    print(n)

#-parcours des deux  à fois
for k,v in dico1.items():
    print("La letre {} correspond la {} ème de l'aphabet".format(k,v))

#Les dictionnaire avec les parametre de fonction

def inc_comp(*liste,**dicot):
    """Cette fonction peut être appelé avec un nombre illimité d'argument
    -les argument non nommés seront stockés dans la liste(*liste)
    -et les argument nommés dans le dico(**dicot)


    """
    nl=len(liste)
    nd=len(dicot)
    print("J'ai recut {} parametres nommés {} de parametre non nommé\
".format(nd,nl))

#Transformer un dico en parametre nommé d'une fonction

para = {"sep":"Michel","end":"Fin"}

print("Voici tu vois", "un", "exemple" , "d'appel", **para)
#Puisque print devrait separer les éléments qu'il recoit par la valeur de 'sep'
#il va maintenant prendre la valeur défini dans le dico, là où il doit mettre
#espace comme valeur de sep il va mettre ce qu'on a donné à sep comme valeur
#dans le dico

    
    
    


