#coding:utf-8

"""
Quelque remarques sur les boucles
    les mots:
        continue : permet de remonter au début de la boucle pour reévaluer la contidions de la boucle
        break : permet de quitter dans la boucle quelque soit
"""

#boucle while
compteur = 0

while compteur<7:
    print("On est encore dedans")
    compteur +=1


jeu_lance = True

while jeu_lance:
    choixMenu = input(">")

    if choixMenu =="again":
        continue

    elif choixMenu =="quit":
        break

    else:
        print("Commande introuvable!")


print("A bientôt ...")


#La boucle for
sentence = "Bonjours frères et søeurs"
for letter in sentence:
    print(letter)


print("A bientôt encore !")


