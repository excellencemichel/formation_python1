#coding:utf-8

"""
Pour la bonne pratique doit être sensée faire qu'une chose à la fois
Une fonction commence toujours par le mot clé 'def'
 comme les variables, les fonction doivent avoir un nom avec
 les mêmes recommandation de nommage
"""


def dire_bj():
    """
    Une fonction quand elle est définie, il reste à
    l'appéler pour qu'elle puisse jouer le rôle qu'on
    a assigné
    :return:
    """
    print("Alléluia !")


dire_bj() #Appel de la fonction

#Les fonctions avec les paramettres
def dire(nom_personne, message, age_personne=25):
    """
    Une fonction avec paramtre mais qui fait juste son
    activité mais ne retourne rien
    les paramtres naturels lors de l'appel de la fonction
    s'ils sont pas fourni python lève une erreur
    Mais s'il y a des parametre qu'on veut définir par
    défaut au cas où se parametre sera absent qu'on est une
    valeur par défaut on doit nommer ce parametre dans la
    fonction
    Lors de l'appel de fonction il peut arriver qu'on appel
    pas les argument dans le même ordre qu'on les a définit
    dans la fonction et la python peut intervertir les chose
    ce qui peut avoir pour conséquence ici : le nom de la
    personne prend la place du message et vis versa
    pour remedier à cela il qu'en appellant la fonction
    on désigne les argument avec leur valeur
    :param nom_personne:
    :param message:
    :return:
    """
    print("{} (âgé de {}); {} ".format(nom_personne, age_personne, message))


dire("Michel", "dit bonjour à la famille !") #Laisse la valeur par défaut à age_personne

dire(25, "Salut", "Excellence") # il y aura interversion des roles

#Pour remedier à celà l'appel de la fonction doit donner
#au argument leur même dans le désordre ça ne pausera pas
#de problème
dire(age_personne=23, nom_personne="Excellence", message="salut à vous !") #Ici quelque soit l'ordre des arguemnt, python trouvera le bon plan





#Fonction qu'on ne connait pas d'avance le nombre de parametre
def show_enventory(*list_items, **dico_items):
    """
    Si nous ne connaissons pas le nombre de parametre à
    l'avance il suffit juste de mettre * (étoite) devant
    le parametre
    Ces parametre seront stockés dans une liste
    comme les liste ne sont pas faites de clés et valeurs
    c'est la partie des dictionnaire, les clés et valeurs
    si on veut donner des paramettre nommés on met ** (deux étoiles)
    :param list_items:
    :return:
    """

    print("J'ai eu {} nombres d'arguments les voici :".format(len(list_items)))
    for item in list_items:
        print(item)


    for key ,value in dico_items.items():
        print("La clé '{}' a eu pour valeur ->'{}'".format(key, value))


show_enventory("Michel", "Excellence", "Bienvenue", nom="Bienvenue")


#Fonction avec les valeur de retour

def calculer(nb1, nb2):

    return nb1 + nb2


calculer(12,7)#Ici puisque la fonction returne quelque,
#La fonction fait seulement son traitement
#Si on veut avoir la réponse il fat alors stocker la réponse
#dans une variable

resultat = calculer(40, 77)
print(resultat)
