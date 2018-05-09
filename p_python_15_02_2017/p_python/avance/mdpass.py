#! /usr/bin/python2
#-*-coding:utf-8-*-

#Les mots de passe
from getpass import getpass #Pour demander le mot de pass

import hashlib

"""
La gestion des mots de passe passe par le module 'getpass'
   Avec la fonction on demande une saisie à l'utilisateur,
   cette saisie est retournée par la fonction qu'on peut éventuellement stockée
   dans une variable
   cette fonction  réagi comme 'input()'


"""

md_pass=getpass("Tapez le mdp :")

#Exemple de hashase de mot de passe

md_passe = b"AzertY" #Le 'b' devant permet de rentre la chaine en byte car
                     #la méthode de hasshase utilise le byte

md_passe_ch = hashlib.sha1(md_passe).hexdigest()
print(md_passe_ch)

deve =True

while deve:
    entre = getpass("Tapez le mot de passe : ")
    entre = entre.encode() #Permet d'encode la saisie en byte
    entre_ch = hashlib.sha1(entre).hexdigest()
    print(entre_ch)

    if entre_ch == md_passe_ch:
        deve = False
    else:
        print("Mot de passe incorrect !")
print("Mot de passe correcte !")

        
    

