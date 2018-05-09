#les métaclass

#Le fonctionnement d'une classe est plus compliqué qu'on imagine
"""
Le conctruncteur d'une classe n'est pas responsable de la création d'un objet,
mais il initialise l'objet en lui attribuant ses att

La methode spéciale charge de la création d'un objet est '__new__'
Mais pour redéfinir la méthode '__new__' il faut encore passer la classe mère
'object' le soin d'y faire, en passant '__new__' à 'object' pas d'autre chose en
paramètre sinon l'instance de classe ou le nom de la class elle-même


----En python tout est objet---------
---Les classe n'échape pas à cette règle, les classe aussi sont modélisées sur
la classe principale qui la classe 'type', et les classe 'int', 'str',list',
'dict', et même nos propres classe que nous developpons ne font appeler les
méthode leur classe principale 'type',
-le définition d'un contructeur '__new__' fait appel à la methode '__new__' de
'type' et même l'initialiseur '__init__' fait appel à la methode __init__ de la
classe 'typpe'
      ---En fin tout ça c'est par défaut------

Puisque tel est le cas on peut donc créer une classe sans passer forcement par
le mot clé 'class' donc passer directement par la classe principale 'type' par qui
tout lui revient ,
la technique est la suivante :
  -le nom de la classe
  -les classe à hériter dans un tuple
  -les attribut dans un dictionnaire
Tout ce passe comme ça :
    Michel = type("Michel", (a_heriter), {attibut})


--------------------

Les métaclasse permette à des classes de prendre pour métaclasse or la métaclasse
par défaut qui est 'type'

   -Laréation des métaclasse se fait de la même façcon les classes ordinaires
   -Les métaclasse hérite de type
   -Cependant le principe repose sur la méthode spéciale '__new__' et '__init__'
     Les paramètre de la méthode __new__ :
         -la métaclasse servant de base à la création de nouvelle classe
         -le nom de la nouvelle classe qu'on créera à partir de notre néométacla
         -les classe à hériter dans un tuple;
         -les méthodes et attributs dans un dictionnaire

"""

#Exemple d'utilisation de '__new__'

class New:
    """Classe définissant des nouvelles avec leurs:
-nature,
-pays
"""
    def __new__(cls, nature, pays):
        print("Appelle de la méthode __new__ de la class {}".format(cls))
        return object.__new__(New)

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
        return super(Personne,cls).__new__(cls)
    def __init__(self, nom, prenom):
        print("Appel de la méthode spéciale __init__ de l'objet {}.".format(self))
        self.nom=nom
        self.prenom = prenom
        self.age=22
        self.rsi="Zaly"



#____________________________________________
#La construction d'une classe sans passer par la clé 'class'

def creer_personne(personne, nom, prenom):
    """ La fonction qui va prendre le rôle de contructeur
'personne' prend la place de 'self'
"""
    personne.nom= nom
    personne.prenom=prenom
    personne.age=21
    personne.rsi="Komata"

def presenter_personne(personne):
    """Fonction chargée de presenter la personne """
    print("Il s'appel {} {}".format(personne.nom, personne.prenom))

methodes={ #Le dictionnaire qui va contenir les méthode et les attributs
    "__init__":creer_personne,
    "presenter":presenter_personne,
    }

Perso =type("Personne", (), methodes)


#_________________________
#Les métaclass
#Les métaclasse permette à une classe de prendre pour métaclasse autre que la
#métaclasse 'type' qui est la métaclasse par défaut

class Metaclass(type):
    def __new__(mtcla, nom, bases, dict):
        """ Création de notre classe,
Lorsque la classe sera créée au lieu la __new__' de type soit appelée c'est
maintenant la '__new__' définie ici qui sera appelée car on a hériter de 'type'
et on a redéfini sa méthode __new__
"""
        print("On crée la classe {}".format(nom))
        return type.__new__(mtcla, nom, bases, dict)

    def __init__(cla, nom, bases, dict):
        """ Methode permetant d'initialiser les classe quand elle vienne d'être
créée frêchement par __new__
"""
        print("Nous avons initilisé {}".format(nom))
        return type.__init__(cla, nom, bases, dict)


class Mc(metaclass=Metaclass):#Ce nom 'metaclass' ne  change pas
    """ Ce nom 'metaclass' passé en parametre de la classe pour montrer que la
classe va predre pour métaclasse pas type mais notre propre métaclasse qui
'Metaclass'
Puisqu'on a déjà créé la classe le constructeur sera appélé à l'exécution de
la fonction
"""
    pass



#____________________
#Application des metaclass
#Une metaclass servant de une alborescence (bibliothèque")
dico_classe ={} #dictionnaire qui va contenire les classe créées

class Mbiblio(type):
    """ C'est la méthode de toutes les classe de la bibliothèque
    """
    def __init__(classe, nom, base, dict):
        """ Méthode qui sera appelée quand on créera une classe issue de la
        bibliotèque
        Toutes les classe prenant cette métaclasse à la place de type, elles
        et les classe leur héritant aurons pour métaclasse bien-sûr la métaclass
        'Mbiblio'
        
        """
        type.__init__(classe, nom, base, dict)
        dico_classe[nom]= classe # Ici nous faisons d'une sorte qu'à chaque fois
                                 #une clalsse est créée elle soit stockée dans
                                 #ce dico, 'cle=nom_de_la_classe', valeur=classe
                                 #elle_même'
        
#On peut également faire de plus avec les métaclass car c'est le principe de
#de la création des bibliothèque comme les bibliothèque de la création des
#interfaces, photo et tant d'autres...

dico_widget ={}
class Mawidget(type):

    """
    Métaclasse pour la cration des widgets
    """
    def __init__(clas, nom, bases, dict):
        """ Contructeur des widgets """
        type.__init__(clas, nom, bases, dict)
        if nom not in dico_widget.keys(): #ça permet le controle de ne pas le
                                          #même bon de classe 2 fois
            dico_widget[nom]=clas
        else:
            raise TypeError("Ce nom existe déjà ici")
        

        
        

        
