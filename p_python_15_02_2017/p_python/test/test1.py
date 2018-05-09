#Les tests

import unittest

"""
Les tests, mise en place des tests

  Pour créer un test, si on veut effectuer les test de type unitaire
  on doit créer une classe héritant de la classe 'unittest.Test.Case'

    Le nom de toutes les methodes permettant d'effectuer doit commencer par
    test avent toute autre lettre

    Il y a une méthode qui est appelée avant toutes autres méthode de la classe
    héritant de unittest.Test.Case 'setUP' c'est donc elle que unitest appel avant
    les autres methodes de la classe

    Si on a une varible qui sera utilise pour toutes les méthodes de la classe
    on peut la définir dans cette methode


"""


#Pour commencer, on va tester le fonctionnement des fonctionnalités d'un odule
#standard de python le module 'random'
import random


#La fn choice qui permet de choisir un élément par hasard parmis une sqce
liste1= ["Michel","Mathieu","Marc","Luc","Jean","Jacques","Pierre","André"]
hasard=random.choice(liste1)
print(hasard)
liste1
print(liste1)



#La fn shuffle qui permet de melanger les éléments d'une sequence
random.shuffle(liste1)
print(liste1)

#Prendre un ensemble d'éléments dans une seq hasarement
en_hasarement=random.sample(liste1,7)
print(en_hasarement)


#Mise en place de test sur les fonctionnalité de module 'radom'

class RandomTest(unittest.TestCase):
    #Le test de la fn choce
    def test_choice(self):
        """ Test le fonctionnement de la fn 'random.choice' """
        liste = list(range(10)) #Créé une liste apartir des nombre renvoyer par range
        elt= random.choice(liste)
        #Verifie que elt est dans liste, puisque c'est de la qu'il été tiré
        self.assertIn(elt, liste)


    #Le test de la fn shuffle

    def test_shuffle(self):
        liste2= ["Adam","Noé","Abraham","Moise","Jésus"]
        liste2.sort()
        print(liste2)
        random.shuffle(liste2)
        print(liste2)
        liste2.sort()
        print(liste2)
        liste3 = list(range(10))
        random.shuffle(liste3)
        liste3.sort()
        self.assertEqual(liste3, list(range(10)))


    #Le test de la fn sample

    def test_sample(self):
        liste4 = list(range(10))

        extrait=random.sample(liste4,3)

        for elt in extrait:
            self.assertIn(elt, liste4)

        #self.assertRaises(ValueError, random.sample, liste4, 20) #Sans contexte manager
        #Avec context manager
        with self.assertRaises(ValueError):
            random.sample(liste4, 20)

#unittest.main()


class RdTest(unittest.TestCase):

    """ Nouveaux tests des methode de random en utilisant 'setUp' """

    def setUp(self): #Cette methode est appelé avant toute methode
        self.liste5 = list(range(10)) #Cela permet d'avoir la liste dans toutes les meth

    def test_choice(self):
        hasard=random.choice(self.liste5)
        self.assertIn(hasard, self.liste5)

    def test_shuffle(self):
        random.shuffle(self.liste5)
        self.liste5.sort()

        self.assertEqual(self.liste5, list(range(10)))

    def test_sample(self):
        extrait = random.sample(self.liste5,7)

        for elt in self.liste5:
            self.assertIn(elt, self.liste5)

        with self.assertRaises(ValueError):
            random.sample(self.liste5, 20)



#unittest.main()


