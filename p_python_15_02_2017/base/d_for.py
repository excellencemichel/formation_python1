#Cette partie explique les mécanisme derière la boucle 'for'

"""
 Le mécanisme des iterateurs, python à une methode spéciale qui permet de
 parcourir un objet conteneur
 Chaque objet conteneur à sa méthode spéciale qui se nomme '__iter__' qui est
 sert à créer l'interateur qui permet de créer l'itérateur qui nous aide à
 parcourir des objets conteneur,
 l'objet iterateur a une la méthode spéciale '__next__ qui lui permet de
 parcourir d'élément en élément des objets conteneurs

 Python utilise des méthode 'iter()' pour appeler la m-s '__iter__' d'un objet
 conteneur et 'next()' pour appeler la m-s '__next__' de l'iterateur créé par
 '__iter__' , 'next()' sert à parcourrir les élément de l'ob conteneur par défaut
 de gauche à droite

 On peut aussi utiliser les générateur pour créer des itérateurs, les générateur
 utilise le mot-clé 'yield' qui renvoie la valeur qu'on lui donne
 cela permet de créer un iterateur à chaque 'next' le yield passe à next la
 valeur prochaine et la fonction s'arrete, le prochain next yield passe encore
 valeur prochaine à next ainsi de suite jusqu'à arrivé à la fin, la fonction
 lève l'exception (erreur) 'StopIteration' qui signifie qu'on est à la fin de
 l'obet iterateur
 la fonction est à exécuter
"""

li=[1,2,3,4,5,6,7]

it_li=iter(li) #construction d'un objet iterateur, ici c'est la m-s '__iter__'
             #de la liste 'li' qui est appelée
next(it_li) #appel le prochain élément dans la liste de gauche à droite
           #, ici c'est la m-s '__next__
            #de l'ob iterateur 'it_li' qui est appelée

#Tout comme pour les chaine de caratères c'est le même mécanisme

ch="Salut je suis le gueek"
it_ch = iter(ch) # création d'ojet iterateur de la str et donnc appel de la
               #m-s '__iter__'

next(it_ch) #Affiche le prochain élément dans la chaine de gauche à droite
            #, donne à la m-s '__next__'
            #de l'ob iterateur 'it_ch'

#Puisse les iterateur des ob conteneur sont issu des classe on peut faire des
#faisant la même chose ou son contraire

class RevStr():
    """
     Classe éritant de str (classe mère des chaine de caractères) mais qui va
     redéfinir la m-s '__iter__' qui est appelée quand on créé un iterateur d'un
     ob conteneur provenant de 'str'
     Mais dans cette classe nous allons faire le l'inverse des parcours au lieu de gauche
     à droite on va faire de droite à gauche

    """
    def __init__(self, chaine):
        self.chaine = chaine
        self.position = len(chaine)

    def __iter__(self):
        """Cette méthode revoi un iterateur parcourant la chaine de gauche à
         droite dans le sens invers de 'str'
         """
        return self #On renvoi l'iterateur créé pour l'occasion
        #Quand on veut develloper la méthode '__next__' dans une autre classe
        #on pourait l'appelé comme ça : return ItRevStr(self) alors c'est cette
        #C'est class qui fournirait l'intérateur, la class ici pourait heriter
        #de 'str' et l'ob se cré de nature str , son aff avc repr et print est
        # prérèglé, alors ici c'est le constructeur qui determine la nature de
        #l'objet donc lors de l'instanciation, si on passe une liste à la class
        #le parcours de fait à la façcon des liste, si c'est un 'str' on bascule
        #vers la façon de parcours des 'str'

    def __next__(self):

        if self.position ==0:
            raise StopIteration("Vous êtes à la fin")
        self.position -=1

        return self.chaine[self.position]

class ItRevStr:
    """
      Un iterateur permetant de parcourir une chaine de la dernière lettre
      à la 1ère . On stocke dans des attributs la position courante et la
      chaine à parcourir
     
    """

    def __init__(self, chaine):
        """ On se positionne à la fin de lachine dès la construction de l'ob

        """
        self.chaine = chaine
        self.position = len(chaine) #On prend le nombre de caractère contenant
                           #dans l'objet créé

    def __next__(self):
        """
         Cette méthode doit renvoyer l'élément suivant contenu dans l'ob
             conteneur dans le parcours,
             ou lever l'exception 'StopIteration' si le parcour est fini
        """

        if self.position ==0:
            raise StopIteration("Tu est arrivé à la fin de l'iterateur")
        self.position -=1 # On décremente à chaque fois '__next__' est appelé
                             #cela permet d'aller toujour du plus grand au plus
                             #petit
        return self.chaine[self.position]# L'envoi de l'élément suivant, ici
                          #qui va être  l'élément précédent vu que l'ordre est
                          #renversé


#______________________
#Le système de parcours avec les générateurs
#Les fn générateur


def fg():
    """ Génarateur qui renvoi simplement les valeurs qu'on donne au mot-clé
    yield
    """
    yield 1
    yield 2
    yield 3
#La fn est à exécuter pour donner l'obet itérateur
#la fonctio peut être exécuter dans une variable, comme ci 'var =fg()
#cette var devient itérable on peut même la parcourir par la boucle 'for'
#La fonction peut être exécuter dans une boucle 'for' ce qui donne le même re-
#sultat, cela se fait comme si : for nb in fg():
                                     #faire ce qui a à faire

#On peut faire plus avec les générateurs

def intervalle(bi, bs):
    """ Générateur parcourant la serie des entiers entre bi et bs
    La bi doit être inferieur à bs
    """
    print("Michel")

    bi +=1 # La bi doit être inf à la bs à chaque appel de la fn augmentant 1 à1

    while bi<bs:
        valeur_recue= (yield bi)
        if valeur_recue is not None:
            bi = valeur_recue
        bi +=1

        
        
    

        

        
        


     

