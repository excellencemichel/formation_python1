#coding:utf-8

"""
Les propriétés sont les entité par eux
on passe pour faire actions sur des objets
de la classe
"""


class Personne:

    def __init__(self, nom, prenom):
        """
        Par convention un attribut qui doit avoir des restriction
        doivent commencer par un _
        juste une convention des développeurs
        :param nom:
        :param prenom:
        """
        self.nom = nom
        self.prenom = prenom
        self._age = 23
        self._domi = "Marrakech"


    def _getage(self):
        print("Récupération non autorisée")

    def _setage(self, nl_age):

        print("Attention ! modification de l'âge")
        if nl_age <0:
            print("L'age ne peut pas être inferieur à zero")
            self._age = 0
        self._age=nl_age

    age = property(_getage, _setage, "C'est l'âge de la personne")

    def _getdomi(self):
        print("Tu cherche à connaitre notre domicile? Le voici :")
        return  self._domi

    domi = property(_getdomi)



print("Lancement du programme")

perso1 = Personne("Loua", "Excellence")

perso1.age

print(perso1.age)


print(perso1.domi)

perso1.age = -1

help(Personne.age)


