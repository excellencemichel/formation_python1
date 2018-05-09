#Compréhention des listes
#La création des liste se fait avec les crochets '[]'

li = ["a","b","c","d","d"]

#Parcours des listes
"""
-Parcours simple avec la boucle for :
 une néo-varible créée par for (souvent nommée 'n') prend successivement les
 éléments de la lite

-Parcours avec la méthode des liste 'enumerate':
  cette methode des liste créé deux variable:
    -l'une contient la position des éléments dans la liste alors que
    -l'aure prend la valeur des éléments de la liste aussi successivement
-Affichage des éléments de la liste
  -On peut afficher les élément d'une liste à travers leur position dans la liste
  cela ce la fait simplement avec l'élément de création d'une liste '[]'
  avec l'intervalle ouvert à gauche et fermer à droite

-Transformer une liste en chaine de caractère: Cela se fait avec la methode
liste 'join()'

_________________________
-Liste et parametre de fonction de foction
  si on veux construire une fonction dont on ne connait pas d'avance le nombre
  d'argument non nomé qui doit lui être fourni, on les met dans une liste ,
  pour cela on passe à la fonction le parametre qui doit stocker les arguments
  qui seront fourni juste avec une asterite(start ou étoile) *
  mais cela ne permet pas de prendre des parametres nommés, c'est la partie des
  dictionnaires
  si la fonction doit prendre des parametre normaux et des parametres nommés,
  on place les parametres normaux avant le parametre avec * et les parametres
  nommés après le parametre avec *
----------------------
-On peut également transformer une liste en parametre de fonction,
si fonction doit prendre parametre on peut créer une liste qui prend ces param
et donner à la fonction qui remplacera ses parametre
--------------------------------
"""
#Avec simple for
for n in li: # Comme ça la varible n créée par for prend successivement les
             #les valeurs prises stockées dans la liste
    print(n)
    
#_________________________________________________
li1 =["a","b","c","d","e","f","g","h","i"]
#Avec  la méthode des liste 'enumerate' qui va avec for seulement créé 2 var
for n,elt in enumerate(li1): #Ici 'n' prend la position dont chacun des éléments
                            #occupe et ça successivement
                           #Alors elt prend la valeur des éléments (éléents eux-mêmes)
                           #et ça encore successivent comme 'for' simple
    print("La lettre {} occupe la {}er(em) position dans la liste \
de l'alphabet".format(elt,n))


#------------------------------------------------------
#Affichage des éléments à travers leur position
li3 =[1,2,3,4,5,6,7,8,9]
li3[:2] #Prend les éléments du début jusqu'au 2è élément (mathqment [1;2[)
li3[3:] #de la position indiquée (ici '3') jusqu'a la fin de la liste
#Avec les 'debut jusqu'à telle borne[:a] ou de la borne jusqu'à la fin [a:] l'intervalle
   #l'intervalle est toujours ouvert à la borne indiquée donc pas incluse
li3[2:3] #Juste le 3è car l'intervalle est femer à gauche
li3[1:3] #Prend le 2è et le 3è élément vu ]1; 2] 
#A noter que l'intervalle est toujours ouvert à la borne superieur cela du fait que
#le comptage ce fait à partir de '0'






#-----------------------------------------------------------------------------
#liste comme parametre de fonction

def liste(*element): #Une telle fonction prend un nombre illimité de parametres
                     #et les stock dans une liste afinÄ un tuple
    #Si la fionction à besion de prendre d'autre parametre, ceux ci doivent être
    #mis avant le parametre portant *
    l=len(element)
    print("On m'a appépé avec {} parametres".format(l))




#------------------------------------------------
#Avec cette procedure on va devoir copier le fonctionnement de la fonction print qui
#recoit tout élément n'importe lequel et les affiche en les séparent avec des espaces

def cprint(*parametres, sep=" ",end="\n"):

    #puisque les éléments sont tuple et que les tuples ne sont pas modifiable
    #on va les modifier en 'list' pour pouvoir travailler dessus
    parametres = list(parametres)

    for n, parametre in enumerate(parametres):
        parametres[n] = str(parametre)
        print(type(parametre))

    #donc tous les élément de la liste sont transformés en 'srt'

    #on peut metentenant transformer la liste total 'parametres' en str pour l'afficher'

    chaine = sep.join(parametres)

    chaine +=end #Pour faire retour à la liste à chaque fin

    print(chaine)



#---------------------------
#Transformer une liste en parametre d'une fonction

liste2=["Bj","à tous"]
print(*liste2) #Print prend la liste comme les parametre qui devaient lui etre fourni




#__________________________________________________

#Les liste avec parametre de fonction on ne peut pas prendre les paramtres
    #nommés (para=b


#Transfomation de liste en chaine
liste1 =["Bonjour","à","tous","tout genre","confondu"]
" ".join(liste1)# cela transforme la liste en 'str' et separant les éléments de
               #de la liste par des 'espaces'
               #On peut lui donner n'importe quel autre élément qui servira
               #d'élément séparateur
michel= "Michel".join(liste1) #Hhhhhhhhh



#_________________________________________________
#Suppression d'élément de la liste
#A travers leur position les éléments de la liste peuvent être supprimé avec
#précision
#Tout ce fait avec le mot clé 'del'
liste2=["o",0,1,2,3,4,5,6,78,9]
del liste2[0] #Va supprimer le 1er élément de la liste
#Après le rang des éléments se déplace ceux de derrière la position de l'élément
#effacer prenne la position suivante

    
    

    




    
