#codind:utf-8

"""
Une classe créé sans l'instanciée équivaut
à la définition d'une fonction sans l'appéler
celà ne donne aucun effet
Un attributs est une variable de classe
"""



class Humain:
    """
    Une classe pour comprendre les
    attributs de classe
    """

    #Attribut de classe c-a-d elle n'appartient pas à une
    #Methode spécifiquement ni à un objet en particulier
    #Son accès ne passe pas alors par self
    #Cela ce fait par le nom même de la classe
    humain_cree = 0
    def __init__(self, c_prenom, c_age):
        self.prenom = "Michel"
        self.age = 18
        self.c_prenom = c_prenom #Appartenant à la classe
        self.c_age= c_age
        print("Crétion d'un humain {}".format(self))

        Humain.humain_cree +=1



print("Lancement du programme ...")

h = Humain("Excellence", 17)

h1 = Humain("Excellence", 23)

print("Le prénom de h1 -> {} et il est âgé de {} ans ".format(h1.c_prenom, h1.c_age))

print("Humain existants : {}".format(Humain.humain_cree))

h3 = Humain("Pierre", 22)

print("Humain existants maintenant : {}".format(Humain.humain_cree))

