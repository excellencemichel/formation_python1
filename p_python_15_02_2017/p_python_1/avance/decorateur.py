#Les décorateurs

"""
 Les décorateurs sont des fonctions clasique de python, ont les défini comme des
 fonction ordinaires;
 Les décorateurs servent à modifier le comportement par défaut des fonction or-
 dinaires
La seule # est que les décorateur prenne en parametre une fonction celle qu'il
va modifier
 et renvoi une fonction :
    -soit la fn en parametre dans ce cas le comportement de la fonction
    en parametre ne sera pas altéré
    -soit une autre fonction, dans ce cas le comportement de la fonction en
    parametre sera altéré pas par la fonction renvoyée par le décorateur
 
 
A noter les décorateurs sont appelés lors de la définition de la fn qu'ils vont
modifier et non à l'appelle de la fonction qu'il vont modifier

Les décorateurs peuvent aussi décorée les classe, cela se passe également comme
les fonctions, à la définition de la classe le decorateur est appelé

On peut décorer une fonction ou une classe par un ou plusieurs décorateurs en
mettant la liste des décorateurs avant la définition de la fonction ou la classe
    -@deco1
    -@dec2
    -@dec3

Si la fonction qui va remplacer la fonction décorée prend des parametres la fonct
décorée doit aussi prendre des parametres
"""


#Définition d'un décorteur

#Décorateur qui n'altère pas le comportement de la fn en parametre
def decorateur(fonction): #Même définition standard avec les fn ordinaires
    print("C'est le décorateur 1 qui a décoré la fonction {} .".format(fonction))
    return fonction #Ici le comportement de la fonction ne sera pas modifié car
                   #c'est la fonction à modifier qu'on a appelé donc son appel
                   #est normal sans altération
@decorateur #On appelle le décorateur 'decorateur1' sur la fonction qui suis
def sans_alt():
    print("J'ai pris le décorateur mais mon fonctionnement n'a pas été modifié")



#Décorateur qui modifie le comportement de la fonction en parametre
def decorateur1(fonction1):
    def fn_modifie():
        print("C'est moi qui ai modifier le comportement de la fonction {}\
 pour qu'elle affiche mon message dont vous voyez.".format(fonction1))
        return fonction1 # Cette fonction se charge de returner la fonction
                        #décoré sinon la fn décorée ne fera jamais son travail
                        #propre à lui
    return fn_modifie() # Quand on décore c'est cette fontion 'fn_modifie' qui
                      # sera appelée

def salut1():
    print("Je dois vous dire salut si on m'empeche pas")
#appel du décorateur sur la fonction salut
salut1 = decorateur1(salut1) # ce la revient au même que quand on met @decor au
                           #dessus de la définition de  la fonction

#exemple de décorateur empechant l'exécution de la fonction décorée

def decorateur2(fonction2):
    def fonction_qui_empeche():
        raise RuntimeError("Cette fonctuion que vous utiliser est obselete")
    return fonction_qui_empeche #On doit se contenter de retournerjuste le nom
                                #de la fn sans mettre les parenthèses sinon la
                         #la fn sera appelé à peine l'exécusion du programme
                         #car l'excusion du programe créé la fn décorée et appel
                         #le decoration,
                         #comme ça sans les parenthèse on laisse le soin à la
                         #à la fn decorée d'appeler la fonction qui modifie
                                

@decorateur2
def empeche():
    print("Un message si on ne m'empêche ")

"""
Plus loin un décorateur qui calcule le temps d'exécusion d'une fonction

"""
#On importe le module time qui contient la fonction qui calcule le temps passé
#depuis 1970 jusqu'aujourd'hui

import time

def controle_temps(nb_sec):
    """ Ceete fonction est le décorarateur"""
    def decorateur3(fonction_a_executer):
        print("ça passe par moi d'abord")
        """ Le décorateur qui sera appelé lors de la création de la fn décorée
        """

        def fonction_modifie(*liste, **dico):
            print("Réellement c'est moi qui suis appelée")
            temps_avant = time.time() #Contient le temps de 1970 au début de
                             #de l'exécution de la fonction décorée
            #On appelle la fonction décorée pour pouvoir calculer le temps
            #problable de la fin de son exécution
            valeur_renvoyee = fonction_a_executer(*liste, **dico) #Appel de fn décorée
                                                   #C'est cet intervalle est appelé la fn décorée

            temps_apres = time.time() #Contient le temps entre 1970 jusqu'à
                              #la fin de l'exécution de la fn décorée
            temps_mis = temps_apres - temps_avant
            if temps_mis > nb_sec:
                print("La fonction {} a pris {} pour s'exécuter .\
".format(fonction_a_executer, temps_mis))
            return valeur_renvoyee
        return fonction_modifie
    return decorateur3


@controle_temps(0.5)
def salut2():
    input(" Tapez Entrée : ")


#Toujours dans le soucis de la performance

def ctl(nb):
    def deco(fn):
        def fnm(para):
            t_av = time.time()
            v_r = fn()
            t_ap=time.time()
            t_e = t_ap-t_av
            if t_e<nb:
                def fat():
                    lettre=input("Tapez 'q' :")
                    while lettre.lower() != "q":
                        lettre =input("Tapez q")

                return fat()

            elif t_e>nb:
                print("La fonction {} a pris {} de temps pour s'exécuter".format(fn,t_e))
            return v_r
        return fnm
    return deco

@ctl(5)
def salut3():
    input("Quelques lettres de l'alphabet mon frère :")
    


def dec(cls):
    print("Définition de la classe {}".format(cls))
    return cls

@dec
class C:
    pass



#Application des décorateur
#Une classe ne créant qu'un seul objet

def singleton(clas_un):
    dico_objet = {} #Ce dictionnaire stockera sur sa clé la class qui sera décoré
                  #et sur sa valeur les objets créés à partir de
                    #la class décorée
    print("1",dico_objet)
    def get_dico_objet(): #fonction testant si le nouveau objet n'est pas dans le dico
        if clas_un not in dico_objet: #Si l'instance de la classe n'est pas dans
                                   #n'est pas dans le dictionnaire alors
            dico_objet[clas_un] = clas_un() #l'objet créé est le même que le premier
            print("2",dico_objet,dico_objet[clas_un])
        return dico_objet[clas_un] #C'est toujours le même objet qui est renvoyer
    print("3",dico_objet)
    return get_dico_objet

@singleton #Toute classe décorée par singleton n'aura qu'un seul objet
class A:
    def __init__(self):
        self.nom = "Loua"

    def af(self, prenom):
        print("Il s'appelle {} {} !".format(prenom,self.nom))

class B:
    def __init__(self, nom):
        self.nom = nom
        self.age=20

    def af(self,vil):
        print("C'est {} agé de {}, il vient de {}".format(self.nom,self.age,vil))


#Décorateur qui permet  une fonction de controler les types d'argument reçu


def controle_types(*a_args, **a_kwargs):
    """On attend en parametre du décorateurs les types souhaités, On accepete
une liste de parametres indéterminés, etant donné que la fonction modifiée pour
ra être appelée avec un nb vatiable de parametres et chacun doit être controlé
"""

    def decorateur_type(fonction_decoree):
        """decorateur qui renvoi la fonction qui va controler les type"""

        def fn_q_mod(*args,**kwargs):
            """Fonctio qui modifie le comportement de la fonction modifiée"""
            if len(a_args) != len(args):
                raise TypeError ("Le nombre d'arguments attendu n'est pas égal à ce recu")

            #parcours des arguments recus non nommés (*args)
            for i,arg in enumerate(args):
                if a_args[i] != type(args[i]): #Si un arg attendu n'est pas du
                                        #même type que celui reçu
                    raise TypeError("l'argument {} n'set pas de même type que {}\
 ".format(repr(i), a_args[i]))

            #Parcours de la liste des parametres recu nommés 'kwargs'
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {} n'a aucun type précisé .\
 ".format(kwargs[cle]))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("L'argument {} n'est pas de type {} .\
".format(repr(cle),a_kwargs[cle]))
            return fonction_decoree(*args, **kwargs)
        return fn_q_mod
    return decorateur_type
                
                
                    
                
        


            




        





