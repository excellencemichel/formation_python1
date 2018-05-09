#Fichier contenant les fonctions du jeu de pendu

import os
from pickle import Pickler , Unpickler
from random import choice

from donnees import *

def recup_scores():

    if os.path.exists(nom_fichier_scores):
        with open(nom_fichier_scores, "rb") as fichier:
            pick = Unpikler(fichier)
            scores = pick.load()


    else:
        scores = {}
    return scores



def enregistrer_scores(scores):
    with open(nom_fichier_scores, "wb") as fichier:
        pick= Pickler(fichier)
        pick.dump(scores)

def recup_utilisateur():

    nom_utilisateur = input("Entrez votre nom pour commencer : ")
    nom_utilisateur = nom_utilisateur.capitalize()

    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Nom invalide")
        return recup_utilisateur()
    else:
        return nom_utilisateur
    

def recup_lettre():

    lettre = input("Tapez une lettre : ")
    lettre = lettre.lower()

    if not lettre.isalpha() or len(lettre)>1:
        print("Lettre invalide")
        return recup_lettre()
    else:
        return lettre

def choisir_mot():
    return choice(liste_mots)

def recup_mot_masque(mot_complet, lettres_trouvees):

    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"

    return mot_masque
    
