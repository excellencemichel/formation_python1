#coding:utf-8

"""
Gérer les erreurs
le mot clé try permet d'essayer une chose si c'est bon
on passe mais si c'est pas on essaie les erreurs eventuelles
qui peuvent advenir
try et except vont de pair et eventuellement ( else et finally)
pour que cela fonctionne bien il est bien de savoir les erreur
éventuelle qui peuvent être glissées
"""


ageUtilisateur = input("Entrez votre âge>: ")
#Ici on demande à l'utilisateur de faire rentrer son âge
#Mais rien ne garantie qu'elle peut faire rentrer n'importe
#quoi peut-être même des lettres


try:
    """
    Ici on essaie tranformer l'âge entrer en entier
    mais vu qu'il faut que les caractères entrer doivent être
    des chiffre pour pouvoir les transformer en entier
    au cas ce ne sont pas des chiffre une erreur sera lévée
    c'est là l'interêt de pouvoir les gérer
    """
    ageUtilisateur = int(ageUtilisateur)

except:
    """
    Au cas où ce qui est dans le try n'a pas marché
    """
    print("C'est pas le bon format")

else:
    """
    Au cas où ce qui est dans le try a marché
    ceci peut être mis aussi dans le bloc try ça fonctionne
    de la même
    """
    print("Ahh je vois ton âge est : {}".format(ageUtilisateur))
finally:
    """
    Quelque soit ce qui se passe cette partie est toujour
    exécuteé
    """
    print("Quelque soit l'issu je m'exécute moi !")


#Gerer des exception qu'on prevoit
nb = 12
nb2 = input("Choisir un nombre pour diviser par {} >: ".format(nb))

try:
    nb2 = int(nb2)
    print("Resultat = {}".format(nb/nb2))

except ZeroDivisionError:
    print("Vous ne pouvez pas diviser un nombre par zéro")

except ValueError:
    print("Vous devez entrez de chiffre")

except:
    print("Valeur incorrecte !")

else:
    print("Bravo tout a marché")

finally:
    print("Afin le passage forcé !")


#Lever soit même des exeptions

try:
    age = input("Quel âge as-tu ? >: ")
    age = int(age)

    if age < 18 :
        raise ZeroDivisionError("Vous êtes gamin alors")
    elif age > 70:
        raise ValueError("C'est trop beau pour être vrai")

except ZeroDivisionError:
    print("C'est le message qui la-bas")

except ValueError:
    print("Tu as vu ?")




#Insertion d'erreur

# mois = 12

# assert mois > 3 #Essaie de voir si mois est supérieur à 3 si c'est pas le cas il
# #Lève une exception AssertionError si c'est inferieur à 3
#
# assert mois < 3 #Il essaie de voir si moi est inferieur à 3 sinon
# #Leve une exception AssertionError si c'est superieur à 3

try:
    prix = input("Entrez le prix que vous pensez idéal >:")

    prix = int(prix)

    assert prix<100#Essai de voir si le prix est inferieur à 100
    #Sinon lève l'exception AssertionError
except AssertionError:
    print("C'est trop cher pour ça quand-même")
