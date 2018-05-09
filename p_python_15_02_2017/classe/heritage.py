#Les héritages

"""
 Une classe fille héritant d'une classe mère prend toutes les méthodes de la
 classe mère

    -Une classe hérite d'une classe:
       -si la classe fille à un constructeur, c'est bien-sûr le contructeur de
        la class fille qui sera appelé lors de l'instanciation
        -si la classe fille redéfinie un contructeur en ne prenant pas en
        compte certaint att du const de la c mèr, la c fille n'aura pas accès
        à ces att, pour palier on peut appeller la c mèr dans le const de la
        c fill pour que quand on instantie la c fille , le const de c fille
        pass par la c mèr pour app inplicitement le contruct de la c mèr et
        cela permet de mettre à disposition de la c fille l'essemble des att
        de la c mèr,
        dans les att en commun avec la c mèr sont juste passés en parametre du
        constructeur de la c fille et donné en argument de l'appel de la c mèr
        sans pour autant redéfir ces att dans le corps du construt de la c fil
        exp : Mer.__init__(self, att1, att2)
       -si la class fille n'a pas de construct, c'est donc le contructeur de la
       classe mère qui sera appelé


    -Pour savoir si une classe fille est issue
    d'une classe mère on interroge la fonctio:
       'issubclass', qui donne True si vrai , False snon
       exp : class A:
             class B(A)
             issubclass(B, A) =True,
             issubclass(A, B) = False


    Pour savoir aussi si un objet est issu d'une classe ou de sa classe mère
    on interroge la fontion
    'isinstance' exp : b=B()
                   isinstance(b,A) = True
                   isinstance(b,B)=True
                   v=C()
                   isinstance(v, B)=False


Dans le systhème d'héritage multiple, la recherche des méthodes se fait d'ab
dans la classe qui a hérité, en suite dans les diferentres classe dont la
class a hérité et ce par ordre de classement dans la hiérarchie des mères
passées à la classe fille


Les héritage permettent aussi de créer ses propres classe d'exception puique
les exception sont des classe, il suffit de savoir quelle classe leve quelle
exception
Hiérarchi des exception
'object'->Tous les objets de python
   |
'BaseException' -> Classe mère de toutes les exceptions, dans pas seulement les
                  les erreurs
   |
'Exception' : Exception pour les erreurs

       """


class Uni:
    """
     Classe A, pour illustrer l'exemple d'héritage
    
    """
    def __init__(self, etude, nature):
        self.etude=etude
        self.nature=nature



    
class Fac(Uni):
    """
     Classe Fac, qui hérite de Uni.
     Elle reprend les mêmes méthodes et att de la classe A
    """
    def __init__(self, nom, etude,nature):
        Uni.__init__(self,etude,nature) #Cela permet à l"instanciation on appe-
                                #lle le contructeur de la classe mère pour ne
                                #pas q'on soit privé des autres att de la c mèr
        self.nom=nom

    def __str__(self):
        return "Faculté {} spécialité de {} est {}\
".format(self.nom, self.etude, self.nature)
    def ec(self):
        print("Peut-être")





class Eco(Uni):
    """
     Classe fille héritant de la classe université (Uni)
    """

    def __init__(self, nom, etude):
        self.nom=nom
        self.etude=etude

class E:
    def __init__(self):
        self.n="nom"


class F(Uni):
    pass

#____________________
#Héritage Multiple
class institut(Fac, Eco, Uni):
    """
    Dans cette classe la recherche des méthode se font d'abord dans la classe
    fille ici 'intitut', si la méthode n'a pas été trouvée,
    on va dans la classe 'Fac' on fouille, si le méthode n'y est pas, on
    regarde dans toutes les classe mère de la classe 'Fac'
    si toujours le méthode n'est pas vue on va dans la classe Eco pour fouiller
    dans la même logique et ainsi de suite jusqu'à mettre main sur la méthode
    """
    def __init__(self):
        pass
    



#____________________
#Puisse que les exception ausi sont issues des claase on peut créer des classe
#d'exception liées à un certains cas pricis
#Pour cela il faut savoir la classe des exption et dans quels cas ces exxception
#sont levées pour pouvoir faire hériter sa classe à une exception qui à rapport
#avec l'exception qu'on veut lever



#Pour construire une class qui puisse lever des erreurs elle doit hériter de
#la classe 'Exception' car c'est elle qui s'occuppe des erreurs

#Class d'erreur
class ErreurAnalyseFichier(Exception):
    """
    Cette exception est levée quand un fichier (de configuration) n'a pas pu
    être analysé

    Attributs :
        fichier ---> nom du fichier posant le sousis
        ligne ----->numéro de la ligne posant le sousis
        message --->le sousis qui se pose
        
    """

    def __init__(self, fichier, ligne, message):
        """ Constructeur de la classe exception """
        self.fichier=fichier
        self.ligne =ligne
        self.message = message

    def __str__(self):
        """Affichage de l'exception """
        return "[ {} : {} {}".format(self.fichier, self.ligne, self.message)
    
        

