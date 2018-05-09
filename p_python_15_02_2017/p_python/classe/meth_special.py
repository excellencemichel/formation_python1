#Les méthodes spéciales
from pickle import Pickler, Unpickler

"""
Après les propriétés viennent les méthodes spéciales

_____________
-Par convention toutes les méthodes speciales ont un nom entouré deux underscore
  (__mtsp__)


---------
-Les méthode qui travaillent directement sur c-a-d:
   -lors de sa création et de sa suppression
     -le contructeur : __init__

     -celui qui supprime : __del__: A la # du del propriété qui agit sur les
       att, la __del__ agit sur l'objet même, elle supprime alors que 'del'
       pro supp l'att

"""

class Michel:

    #Les méthodes spéciales

  #Ceux qui agissent directement sur l'objet

    #Le constructeur
    def __init__(self):
        """
           Cette méthode est appelée quand on souhaide créer un sur la plan de
           cette classe
        """
        self.nom="Loua"
        self.prenom="Michel"
        self.age = 22


    #--------------
    #Le supprimeur
    def __del__(self):
        """
          Cette fonction est appelée quand souhaite supprimer un objet de cete
          classe
        """
        print("C'est la fin, l'objet {} est supprimé !".format(self))


    #--------------------
    #Affichage d'objet
    def __repr__(self):
        """
         Cette méthode est appelée quand on souhaite afficher un objet de cette
         classe elle sert donc à modeliser l'affichage des objets de la cls
        """
        return "Nous sommes dans class Michel voici le nom complet du créateur\
 {} {}".format(self.nom,self.prenom)



       #----------------
       #Affichage de l'objet avec print
    def __str__(self):
        """
          Cette méthode est appelée quand on souhaite afficher un objet de cette
          classe avec la fonction print
        """
        return "{} {} agé de {} ans .".format(self.prenom,self.nom,self.age)


    #________________________________________
    #Maintenant les méthodes qui agissent sur les attribut de class

    #Methode speciale '__getattr' : accès à défaut
    def __getattr__(self,nom):
        """
          Cette méthode est appelée quand un objet de cette classe cherche à
          acceder à un att de cette qui n'existe pas,
          à la # des accesseur qui c'est à trvers eux qu'on passe pour acceder
          aux att, mais la meth spl 'getattr' est appéle quand un ob appele un
          att qui n'exite pas
        
        """
        print("Alerte ! il y a pas d'attribut {} ici !".format(nom))


    #------------
    #mth spl 'setattr' : Accès à un att pour le modifier

    def __setattr__(self,n_attr,val_attr):
        """
         Cette méthode est appelée quand on fait ob.n_attr=val_attr
         elle est pendant l'assignation des valeur aux att par le contructeur

         On peut parfois se charger d'enregistrer l'objet
        """
        print("Attention accès pour modification")

        object.__setattr__(self,n_attr,val_attr) #'objet' est la clas mère de
                                            #toutes les methodes spéciale, pour
                                            #une modification de la valeur d'un
                                            #att on doit passer par elle pour
        #eviter de faire une boucle infini, : puisque setattr est appelée dès
        #l'assignation des valeur aux att, donc si on ne passe pas par la class
        #mère , setattr va tenter de changer la valeur d'un att elle vient sur
        #une nouvelle assignation encore encore car c'est comme ça que python
        #foctionne


    #---------------------
    # __delattr__ : Pour la suppresion d'un att
    def __delattr__(self,n_attr):
        """
         Cette methode est appelée quand on souhaite supprimer l'attribut d'un
         objet
         -Ici encore on doit passer par la class mère 'object' pour le faire
            sinon on va recolter des erreur
        -Si on créé cette methode spéciale, si on ne presise pas la suppression
        des att des objets, il ne sera donc pas possible de suppression un att
        de cettec classe
        """
        print("On ne supprime rien ici mon gars")
        #Si on veut supprimer voici la méthode
        #On commente pour que ça ne soit pas possible
        #object.__delattr__(self,n_attr)

        #Si passe par la classe mère 'object' pour la suppression, on créé une
        #boucle infinie
        del self.n_attr



    #____________________________________
#Les méthodes de conteneur
#Nouvelle classe pour commencer cette partie sur des methodes conteneur

class Zdict:
    """
      Classe enveloppe de dictionnaire : c-a-d se passant pour un dico

      -Cela permet d'interadir dans création des objets d'un dictionnaire
    """

    def __init__(self):
        """
         Pas de parametre pour l'intanciation de la classe
         Nous feront de sorte que tout passe par l'attribut du contructeur
        """
        self._dictionnaire={}

    def __getitem__(self,index):
        """
         Cette methode est appelé quand on fait ob.[index]
         Elle redirige vers self._dictionnaire
         c'est quand on cherche à avoir accès à un élément d'un dico à travers
         sa clé qui est ici l'index, cela se passe par cette methode qui
         à elle passe l'elant à l'att du constructeur
        """
        print("Accès à l'élément numero {}".format(index))
        return self._dictionnaire[index]

    def __setitem__(self,index,valeur):
        """
         Cette méthode est appelée quand on écrit ob[index]=valeur
         On redirige vers self._dictionnaire[index]=valeur

         -Egalement cette méthode est appelée quand souhaite créer un élément
         du dico, dont la clé est 'index', la veleur est 'valeur'
         """
        print("Un élément de la liste a été créé, son nom est {} , à la posi\
 tion {} .".format(valeur,index))
        self._dictionnaire[index]=valeur

    def __delitem__(self, index):
        """
        Cette est appelée quand fait del ob[index]
        Elle redirige vers del self._dictionnaire[index]

        cette methode est appelée quand on souhaite supprimer un élément du
        dico

        """
        print("L'élément à la position {} va être supprimé ".format(index))
        del self._dictionnaire[index]

    def __repr__(self):
        return "La clas Zdict qui fait semblant de se passer pour un dico"

    def __str__(self):
        return "Les classe des méthodes de conteneur"

    def __contains__(self, ob):
        """
         Cette méthode est appelé si on veux faire un test sur l'existance 1e
         clé dans l'ob conteneur
         le test se fait sur la clé et non sur la valeur

        """
        if ob in self._dictionnaire:
            print("Oui il y en a")
        else:
            print("Il y en a pas")
        return ob in self._dictionnaire

    def __len__(self):
        """
         Cette méthode est appelée quand souhaite savoir la taille de l'objet

         """
        print("Voici la taille de l'objet conteneur")
        return len(self._dictionnaire)
        

#________________________________
#Les méthodes mathématiques


class Duree:
    """
     Classe contenant des durées sous la forme d'un nombre de minutes et de
     secondes

     Les méthode developpées dans cette classe servent à surcharger les opera-
     teur mathematique

     """

    def __init__(self, min=0,sec=0):
        """ Constructeur de la classe"""
        self.min = min #Nbre de minute
        self.sec = sec #Nbre de seconde

    def __str__(self):
        """Modelisation de l'affichage avec 'print'

        """
        return "{0:02} : {1:2}".format(self.min,self.sec)

    def __repr__(self):
        return "{} min {}s".format(self.min,self.sec)



    def __add__(self,ob_a_aj):
        """
           L'objet à ajouter est un entier, le nombre de secondes
          Avec 'add' l'ajout doit être de l'objet de la classe vers le nouveau
          objet
        """

        nouvelle_duree=Duree()
        #On va copier self dans le nouvel objet qui vient d'être créer pour
        #avoir le niveau pour pouvoir faire l'ajout

        nouvelle_duree.min =self.min
        nouvelle_duree.sec = self.sec

        nouvelle_duree.sec += ob_a_aj
        if nouvelle_duree.sec >=60:
            nouvelle_duree.min += nouvelle_duree.sec //60
            nouvelle_duree.sec = nouvelle_duree.sec % 60

        return nouvelle_duree

    def __radd__(self,ob_a_aj):
        """Pour que l'ajout prenne d'un sens comme d'un autre on ajoute 'r' au
         debut du nom de la méthode
        """
        return self + ob_a_aj

    def __iadd__(self,ob_a_aj):
        self.sec += ob_a_aj
        if self.sec >=60:
            self.min += self.sec //60
            self.sec = self.sec %60
        return self

    #A coté de add qui sert d'ajout il y a aussi les autres opérateur
    #Pour aller plus loin à surcharger les opérateur pour qu'il prennent +=
    #-= on ajoute 'i' au de debut du nom de la méthode
    # -+* // %

    def __sub__(self, a_sus):
        self.sec =self.sec-a_sus
        if self.sec <0:
            self.sec =0
        return self

    def __rsub__(self, a_sus):
        return self.sec -a_sus

    def __isub__(self,a_sus):
        self.sec -= a_sus
        if self.sec <0:
            self.sec =0
        return self
    


    def __mul__(self, a_mul):
        new = Duree()
        new.sec =self.sec
        new.min =self.min
        new.sec = self.sec * a_mul
        if new.sec >=60:
            new.min += new.sec //60
            new.sec = new.sec %60
        return new


    def __rmul__(self, a_mul):
        return self.sec * a_mul

    def __imul__(self,a_mul):
        self.sec *=a_mul
        if self.sec >= 60:
            self.min = self.sec//60
            self.sec += self.sec%60
        return self


    #Ainsi de suite pour
    #'__truediv': /
    #'floordiv' : // (division entière
    #'__mod__': % (modulo
    #'__pow__':** (puissace)



    #_________________________
    #Les méthodes spéciale pour les opérateur de comparaison

    def __eq__(self,a_comp): #Compare l'égalité
        return self.sec==a_comp.sec and self.min==a_comp.min


    def __gt__(self,a_comp): #Compare la superiorité srticte
        nb_sec1 = self.sec + self.min *60
        nb_sec2 =a_comp.sec + a_comp.min*60
        if nb_sec1>nb_sec2:
            print("Il est strictement suprieur")
        else:
            print("Il est plutôt inferieur ")
        return nb_sec1 > nb_sec2


    def __ge__(self,a_comp):
        nb_sec1 = self.sec + self.min*60
        nb_sec2 =a_comp.sec + a_comp.min *60
        if nb_sec1>=nb_sec2:
            print("Il est superieur ou égal")
        elif nb_sec1==nb_sec2:
            print("Ils sont égaux ces objets")
        else:
            print("Il est inferieur ou egal")
            
        return bn_sec1 >=nb_sec2


    def __lt__(self,a_comp):
        nb_sec1=self.sec + self.min*60
        nb_sec2 = a_comp.sec + a_comp.min*60
        if nb_sec1 <nb_sec2:
            print("Il est strictement inférieur")
        else:
            print("Il est plutôt strictement supérieur")
        return nb_sec1 < nb_sec2


    def __le__(self,a_comp):
        nb_sec1 = self.sec + self.min *60
        nb_sec2 = a_comp.sec + a_comp.min * 60
        if nb_sec1 < nb_sec2:
            print("Il est stritement inférieur")
        elif nb_sec1 == nb_sec2:
            print("Il est egal")
        else:
            print("Il est plutôt strictement supérieur")



    def __ne__(self,a_comp):
        ob=Duree()
        if self != a_comp:
            print("Ce ne sont pas les mêmes")

        else:
            print("Ce sont les mêmes")

        return ob != a_comp


#Méthode pour pickler

class Temp:
    """
     Classe contenant plusieurs attributs, dont un temporaire
     
    """

    def __init__(self):
        self.voyage="Moyenne"
        self.etude="Partout"
        self.origine="Zaly"

    def gis(self):
        with open("base.txt","ab") as base:
            pick=Pickler(base)
            pick.dump(self.__dict__)

    def re(self):
        with open("base.txt","rb") as base:
            pick = Unpickler(base)
            self.__dict__=pick.load()

            
    def __setattr__(self,ob,val):
        print('Création')
        object.__setattr__(self,ob,val)
        self.gis()


    def __getstate__(self):
        dict_att = dict(self.__dict__)
        dict_att["origine"]="Komata"
        return dict_att

    def __setstate__(self, dict_attr):
        dict_attr["origine"] ="KOMATA"
        self.__dict__ = dict_attr
        return dict_attr


            
        
        
    
        
        
    
    
            


    


        
        
