#Le triage des objets

#Module de trie
from operator import itemgetter, attrgetter

"""
  Deux méthodes nous sont offertes pour trier des éléments des objets conteneur
    -methode liste: sort()
       Cette méthode ne peut que travailler sur une liste puisque c'est une
       méthode de liste
       -Elle retourne un nouveau objet déjà trié

    -methode builtin de python c-à-d disponible d'office dans python sans avoir
    besion d'un import comme open : sorted()
      Cette methode travail sur n'importe quel ob
      -Elle travail directement sur l'objet sans retourner un nouveau à moins
      qu'on stocke le resultat dans une var

   -Pour ces deux méthodes python tri par défaut par ordre alpahabétique
   A noter les nombre (int) en état de str leur ordre va de 0 à 9 c-à-d
   199999<9, -156545<0, -5552<-9 etc...
   

Les ties peuvent se faire avec les méthodes du module 'operator' qui sont :
   -  'itemgetter' qui prennet en parametre la position de l'élément sur quoi
      le tri va se baser:
      -itemgetter : pour les objets simples (liste, tuple, dico...)
      -attrgetter : pour les objets d'instance (donc des att) 
      

"""

#Méthode de lite sort()
li=["Michel","Mathieu","Fassou","Henry","Benoît","Thomas","Bienvenu","Elie",
    "Aaron"]
print(li)
li.sort() #Tri la liste et revoi un nouveau objet
print(li) #Retourne la liste déjà modifiée car sort() modifi l'objet d'origine

#-------------------
#Méthode de tri d'office de python
li2 = ["Ezékiel","Luc","François","Foromo","Jacques","Loua"]

sorted(li2) #Tri seulement les sequences sans retourne de nouveau objet
print(li2)#Retournera tj l'ob d'org car sorted n'a pas modifié l'origina
li2_tr=sorted(li2)
print(li2_tr)



#-------------------------------------
#Puisque python tri par ordre alphabétique par défaut, pour trié un objet
#contenant un ensemble d'objet # il va falloir personaliser le tri
etudiant = [
    ("Clément", 14,16),
    ("Charles",12,15),
    ("Oriane",14,18),
    ("Thomas",11,12),
    ("Damien",12,15),

    
    ]

#Pour cela on va user sur argument optionel des deux meth sort et sorted : key
#ce arg prend une fn qui doit prendre un élément de l'obet conteneur et retour-
#ne la position de ce sur quoi le tri va se baser, puisque ça neccessite seule-
#ment une courte fn, donc les fn lambda arrangent
sor_pers=sorted(etudiant, key=lambda n: n[2])
print(sor_pers)

etudiant.sort(key=lambda n: n[1]) #Donc la fn lambda nous permet de créer cette
                                #courte fn ananyme
          #lambda prend comme arg n et c'est cet arg qui est passer à l'arg
          #key pour savoir sur il va trier l'objet



#___________________________
#Trie d'objet de class

class Etud:
    """
     Cette classe represente un étudiant.

     On représente un étudiant par son prénom (att prenom), son âge (att age)
     et sa note moyenne (att moyenne, de 0 à 20)

     Paramètres du contructeur:
        prenom ----prenom de l'étudiant
        age -------âge de l'étudiant
        moyenne ---moyenne de l'étudiant

    
    """

    def __init__(self, prenom, age, moyenne):

        self.prenom= prenom
        self.age= age
        self.moyenne= moyenne

    def __repr__(self):
        return "<Etudiant {} agé de {}, moyenne {}\
.>".format(self.prenom, self.age, self.moyenne)
    #Pour trier des objet qui seront créer sur cette class
    def tri(self):
        return sorted(self, key=lambda c : c.moyenne)


etudiant=[
        Etud("Thomas",11,12),
        Etud("Charles",12,15),
        Etud("Oriane",14,18),
        Etud("Damien",12,15),
        Etud("Clément",14,16),
        ]
#Pour trier un objet de classe, il faut juste donner l'att sur lequel vas passer
#Le trie l'arg de la fn lambda comme ceci
#  'sorted(etudiant, key=lambda elt : elt.moyenne)'
#Ici le tri va se faire sur la moyenne de façon accendante,
#Pour faire l'inverse il suffi de preciser une valeur à l'argument optionnel
# 'reverse' si 'True' c'est que c'esr de façon inversée sinon normale



#______________________________
#Les tri avec les méthodes du module 'operator
#Avec le module operator, il suffit de passer en arguent de méthode du module
#l'élément surquel va se passer le tri :
    

    
etu= [
    ("Clément",14,16),
    ("Charles",12,15),
    ("Oriane",14,18),
    ("Thomas",11,12),
    ("Damien",12,15),
    ]
#Pour une liste ou une tupe simplement on met la methode à la place de fn lamdba
#Comme ceci :  'sorted(etu, key=itemgetter(2)) ' comme ça c'est sur la position
# 2 l'élément conteneur que se passera le tri


#-----------
#Avec un objet d'instance on passe en argument de la méthde du module 'operator'
#le nom de l'att sur lequel va se passer le tri sous forme de 'str' toujours à
#place de la fn lambda comme ceci :
# sorted(etudiant, key=attrgetter("moyenne))


#------
#Le trie peut se faire selon plusieur att, on ajoute le nouvel att à la suite
#de l'autres dans les argument de la methode 'attrgetter'




#Autre exemples
class Iv:
    """
     Classe représentant une ligne d'un inventaire de vente.

     Attributs attendus par le contructeur :
     produit ---le nom du produit
     prix ------le prix unitaire du produit
     quantité --la quantité vendue du produit.
    """

    def __init__(self, produit, prix, quantite):
        self.produit=produit
        self.prix = prix
        self.quantite=quantite

    def __repr__(self):
        return "<Ligne d'inventaire {} ({}X{})> \
".format(self.produit, self.prix, self.quantite)


#Création de l'invenataire
    #ceci pour montrer qu'en python matière de tri il y a ce qu'on appelle la
    #stabilité, si on tri deux att, ici prix et quantité, si dux élémens ou ++ ont
    #même prix, python compare les quanté, idem que si deux quantité ou ++
    #sont égale python compare les prix et fait passer le critère des prix.
    #Exp : q(dec), prix(croi) poire vient avant pome rouge,
    # car les prix sont de même mais le critère de quantité passe 

iv= [
    Iv("pomme rouge",1.2,19),
    Iv("orange",1.4,24),
    Iv("banane",0.9,21),
    Iv("poire",1.2,24),
    ]




