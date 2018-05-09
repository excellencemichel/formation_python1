#Les chaine 'srt'

"""
Comme on aime le dire 'En python tout est objet'
les chaine (str) comme tout autre varible de python sont des object
les 'str' ont des méthodes propres à eux

-Mettre les chaine :
                    Majuscule : upper()
                    Minuscule : lower()
                    Mettre en majuscule le debut de phrase : capitalize()
                    centrer dans un espace : center()
_____________________________________________________________________
-Tranformer les chaine en liste:
   C'est avec la methode des chaine 'split'
   cette méthode prend un argument, c'est argument d'élément de partage des
   caractères de la chaine
   si on lui donne espace(" ") chaque caractère deux espaces formeront
   un élément de la liste à commencer du début jusqu'à la fin

________________________________________________________________
-Controle des élément d'une chaine:
  -Ample de methodes servent à connaitre le contenu d'une chaine:
    -exclusivement alphabetique : c'est à dire que de lettre alphabetique a-zA-Z
      'chaine.isalpha()': returne True si chaine est seulment constituée de lettre
      alphabétique, False sinon
      
    ______________

    -exclusivent alphanumeric :c'est  à dire de lettre alphabétique et de nombre
                               a-zA-Z0-9
     'chaine.isalnum()': Returne 'True' si 'chaine est constitué que de lettre
     alphabetique et de nombre, False sinon

    -exclusivemnt numeric :Seulement de nombre entier : 0-9 pas de virgile
      'chaine.isdigit(), chaine.isdecimal()' :Return 'True' si 'chaine est seule-
      que de nombres

    -seulement que de l'espace (donc vide)
     'chaine.isspace()' : Return 'True' si chaine est constituée que d'espaces
     'False' sinon

  -A noter que tous ces doivent exister au moins une fois
  -On a aussi :
    'islower()' : Pour savoir s'il est en minuscule
    'isupper()' : s'il est en majuscule
"""

#Le controle des éléments d'une chaine de caractère
chaine ="Bonjour"
chaine.isalpha()

alnum="Je s8 allé b1sur labas"
alnum.isalnum()

digit="1994"

digit.isdigit()




#Convertir une chaine en liste:
#Cela se fait avec la méthode des chaine : split

chaine1 = "Bonjour tout le monde"

chaine1.split(" ") #traansforme la chaine en liste où les éléents de la liste
#seront constitués par les mots de la chaine, chaque élément s'arrete à chaque
#espace
#Split ne envoit la chaine transformée mais ne change pas la chaine d'orige,
#Donc pour conserver la chaine changée on peut la stocker dans une variable
chaine_en_li = chaine1.split(" ") #chaine_en_li contient la liste envoyée par split




#Parcours des chaine
#Une chaine est elle-même contitué d'éléments : les caracactères qui la compose
#On peut parcourir les chaine avec par exemple la boucle 'for'
chaine2="L'apprentisage n'est pas neccessairement doux mais, le fruit\
 extraordinairement doux"
for n in chaine2:
    print(n)

#Savoir le nombre de caractère d'une chain plus simplement
print(len(chaine2))
