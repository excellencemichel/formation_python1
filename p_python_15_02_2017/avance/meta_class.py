#les métaclass

#Le fonctionnement d'une classe est plus compliqué qu'on imagine
"""
Le conctruncteur d'une classe n'est pas responsable de la création d'un objet,
mais il initialise l'objet en lui attribuant ses att

La methode spéciale charge de la création d'un objet est '__new__'

"""

#Exemple d'utilisation de '__new__'

class New:
    """Classe définissant des nouvelles avec leurs:
-nature,
-pays
"""
    def __new__(cls, nature, pays):
        print("Appelle de la méthode __new__ de la class {}".format(cls))
        return object.__new__(cls, nature, pays)

    def __init__(self, nature, pays):
        print("Appel de la méthode spéciale __init__")
        """Constructeur du new
à vrai dire c'est l'initialiseur
"""
        self.nature = nature
        self.pays = pays
        self.cont="Af"
        self.dom="Privé"


class Personne:
    def __new__(cls, nom, prenom):
        print("Appel de la méthode spéciale __new__ de la classe {}".format(cls))
        return object.__new__(cls, nom, prenom)
    def __init__(self, nom, prenom):
        print("Appel de la méthode spéciale __init de l'objet {}.".format(self))
        self.nom=nom
        self.prenom = prenom
        self.age=22
        self.rsi="Zaly"
        
        
        
