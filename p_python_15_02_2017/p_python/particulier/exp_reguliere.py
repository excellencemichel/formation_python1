#Les expresions regulières en python

from re import *

"""
Le concept des expresions regulière reste le même avec le language php

Les expression sont géréesar le module 're'

 -les essentiels avec les expressions:
 Les expresion regulière sont des recherches et disolement des caractères
  ___________________
  -Recherche au début d'un mot: se fait par le signe  ^ (accent circonflêche)
  -Recherche en fin de mot : par le signe $ (le signe dollar)
    Ces signes vérifient le caractère qu'ils précedent directement, ni après, ni
    avant

    _________________________
   -Controle d'occurence des caractères
      * : 0 , 1 , 2 ... (zéro une fois ou plus)
      + : 1, 2, .. ( une fois ou plus)
      ?: 0,1  (Zéro ou une fois)

      le controle des occurance peut se fait avec  les accolades
       A{3}: 'A' doit y être 3 fois seulement                 Tous en Majuscule
       A{,3} : 'A' doit y être 0 à 3                     On peut faire la même pour les minuscules
       A{3,} : 'A' doit y être au minimun tois fois
       A{1,3} : 'A' doit y être 1 à 3 fois



    -Regoupement des caractère (classe de caractère)
    Pour contrôler un groupe des caractère on utilise les crochets []
    [abcd] signifie que l'une des lettre parmi le crochet
    En utilisant les - on exprimer les classe de cractère
    [A-Z] : toutes les lettres majuscules
    [A-Za-z0-9] : lettre majuscule, minuscule en nombre

    On peut également  contrôler l'occurence des classes de caractère par
    les caractère spéciaux que sont : *, +, ?
    aussi par les accolades:
    [A-Z]{7} : signifie la presence de 7 lettre majuscules qui se suivent

    ____________________
    Les groupe de caractère:
    A la différence des classe de caractère qui contrôle la présence des carctères
    entre ces caractères eux-mêmes, les groupe contrôle la présence effective res-
    pectivent des caractères qui sont indiqués:
    Cela se fait par les parenthèse: ()
    (Michel): Signifie que le mot michel doit effectivement être dans le mot
    (ma){3,7} : 'ma' doit exiter dans le mot 3 à 7 fois et qui se suivent aussi

    ____________________
    On peut aussi faire des recherches et remplacement dans des chaine
    la fonction qui gère 'sub' du module 're'

      -elle prend les parametres suis :
        -l'expression recherchée
        -l'expresision avec quoi on va faire le remplacement
        -la chaine originale qu'on doit faire le remplacement de dans
    
    
    
       
       

"""

#Un regex qui controle le numéro de téléphone
#On va utiliser la fonction 'searh' pour rechercher l'expression qui convient

chaine = ""
expe= r"^0[0-9]([ .-]?[0-9]{2}){4}$" #en fin pour un numéro fraçais

while search(expe, chaine) is None:
    chaine =input("Entrez votre numéro de téléphne : ")


print("ça marche voici ton numero", chaine)

numero=""
controle=r"^6[0-9][0-9]([ .-]*[0-9]{2}){3}$"

while search(controle, numero) is None: #Ici on recherche si le nuero entré est
    #dans conforme à la normale (contrôle)
    numero= input("Entrez un bon format de numéro : ")

print("Ca marche un bon numéro de la guinée")

#Contrôle des email

def cemail():
    imail = input("Entrez votre imail en bon et dure forme : ")
    expression =r"^[a-z]([ -_.]*[a-z0-9]){4,}[@]([a-z]){3,}[.][a-z]{2,4}$"# Le contrôle parfait des émai
    #ici bien-sûr la fn n'est pas bien construite, car l'imail a déjà sa valeur avant
    #qu'on enregistre donc is soit normal ou pas c'est la 1èr valeur qui est enregistré
    #l'essentiel ici c'est le controle des donné reçues
    if match(expression, imail): #On utilise ici la fn match pour savoir si l'ex
        #presion est trouvée dans l'imail
        with open("email.txt", "a") as lesmail:
            lesmail.write(imail)
    else:
        cemail()
    return imail



#________________________
#La recherche et le remplacement

#Pour faure la recherche et le remplacement on utilise la fonction 'sub' toujours
#du module 're'

print(sub(r"Pepe", r"Michel", "Pepe Loua")) # Cette exprepression remplace Pepe par
                                       #Michel

#On peut égélement diviser l'expresion originale en des groupes de caractère
#() pour pouvoir faire le remplacement en foction des numéros de groupe
#la décompte des groupe dépend de l'ouverture et de la fermeture des parenthèses
#elle se fait à partir de 1
print(sub(r"(Nous) ()" , r"\1", "Nous fera ça pour vous")) #Dans ce exemple
                                           #'Nous' a pour numero :1
                                           #'fera' a pour numéro : 2
            #Ici on se contente de rechercher soit le groupe 1(Nous) le remplacer
            #par le groupe 2(fera) vise versa
            #Toutes les expresions de l'originale qui sont dans le groupe s'il
            #n'ont été pas été touvée et mise en remplacement ne vont pas appa
            #raitre dans le resultat c'est comme c'est elles qu'on cherche à
            #remplacer


#___________________
#On peut également nommer les groupe pour pouvoir faire leur distinction
"""
Pour cela on passe la méthode suite :
On fait suivre la parenthèse ouvrante par ? suit d'un P majuscule et du nom du
groupe entre chevron.
Comme ça (?P<nom> a_chercher), tout comme (?P<nom>[a_chercher]{3})
Et maintenant dans l'ewpression de remplacement on utilise les nom des groupes
"""

#Exemple d'aplication

texte = """
nom='Task1', id=8
nom='Task2', id=31
nom ='Task3, id=127"""

print(sub(r"id=(?P<id>[0-9]+)", r"id(\g<id>)", texte)) # Cela signifi siplement
#qu'on cherche 'id=' + nom [0-9]'  pour le remplacer par 'id(nom)



"""
#Plus loin
#Il est aussi possible de garder en memoir des expressions regulières sous
#forme d'un objet pouvan servirt à verifier d'autre données
#si par exemple dans le programme on demande plusieur fois à l'utilisateur
#faire entrer son email ou mot-de-passe et ça trouve c'est la même expression
#regulière qu'on utilise pour le controle, cette technique permet de travailler
#avec la même expression regulière pour sur les autres partie,
# Pour cela on  utilise la méthode 'compile' du module 're'
#Cette methode transforme l'expression regulière en objet ayant des méthode
#comme search ou macth
"""

#Pratique
#Soit un mot de passe qui ne doit comprendre que des chaine et des nombre au
#6 caractères

chaine_pass_controle = r"^[A-Za-z0-9]{6,}$" #Voici les parametre de controle
mdp= compile(chaine_pass_controle) # On compile l'expression dans la variable
     #Cette var est comme un objet qui aura pour méthodes les fn de
     #'re' (search, macth, sub ...)

#Pour utiliser cette expression compilée, on utilise ses méthodes (search, ...)
#contairement aux fonctions de 're' qui prennent en parametre l'expresiion
#tel n'est pas le cas ici car l'expression est déjà dans l'objet

#Contrôle d'un mot de passe
mot_de_pass =""
while mdp.search(mot_de_pass) is None: #Tant que la recherche donne rien
     mot_de_pass = input("Entrez votre mot de passe :")
     







