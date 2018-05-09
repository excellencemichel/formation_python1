#coding:utf-8
"""
Les test basique

"""

def saluer(nom, message):
    print("{} vous dit : << {} ".format(nom, message))



def dire_aurevoir():
    print("Maintenant le programme vous dit aurevoir")




#La condition qui permet de faire des test basiquement

if __name__ == "__main__":
    """
    Cela permet de dire si ce programme est lancé en tant
    que module independant et non importé dans un autre fichier
    pour l'utiliser
    """
    saluer("Excellence", "Bonjour les frères et soeurs en Christ")

    dire_aurevoir()
    print("Ce programme a été lancé en tant que module indépendant et isolément !")
    #Ceci permet de faire des test basic pour savoir que ce
    #a lui seul fonctionne bien avant de faire tout import ailleurs
