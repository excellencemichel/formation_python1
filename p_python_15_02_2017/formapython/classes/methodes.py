#coding:utf-8

"""
Les méthodes sont tout simplement des fonction définies
dans une classe
"""


class Humain:
    """
    Classe Humain pour l'étude des méthode
    """
    lieu_habitation = "Terre"
    def __init__(self, nom, age):
        """

        :param nom:
        :param age:
        """
        self.nom = nom
        self.age = age



    def parler(self, message):
        print("{} a dit << {} >>".format(self.nom, message))

    def changer_planete(cls, nouvelle_planete):
        """
        Cette methode est methode propre à la classe
        c'est pourquoi elle prend en premier parametre
        au lieu de self mais cls
        :return:
        """
        Humain.lieu_habitation = nouvelle_planete


    changer_planete = classmethod(changer_planete)#Désignation de la methode comme methode de classe
    #Le nom de la variable peut ne pas être le nom de la variable de classe


    def definition():
        print("L'Humain est classé comme étant le plus haut être vivant de la chaine animale")

    definition = staticmethod(definition)#Désignation de la methode comme une méthode statique







print("Début du programme")

h1 = Humain("Bienvenue", 23)

h1.parler("Bonne fête les femmes")
h2 = Humain("Excellence", 22)
h2.parler("Courage à vous")

print("Planete actuelle : {}".format(Humain.lieu_habitation))

# Humain.changer_planete("Mars", "Nepturne") #Cela marche au cas où on a pas utiliser classMethod
Humain.changer_planete("Mars")

print("Planete actuelle : {}".format(Humain.lieu_habitation))

Humain.definition() #Cela permet de lancer la méthode statique