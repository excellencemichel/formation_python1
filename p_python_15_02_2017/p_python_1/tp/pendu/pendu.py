#Déroulement du jeu de pendu

from donnees import *
from fonctions import *

scores = recup_scores()

utilisateur = recup_utilisateur()

if utilisateur not in scores.keys():
    scores[utilisateur] = 0


continuer_partie = "o"

while continuer_partie != "n":
    print("Joueur {} : {} point(s) ".format(utilisateur, scores[utilisateur]))

    mot_a_trouver = choisir_mot()

    lettres_trouvees = []

    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver != mot_trouve and nb_chances >0:
        print("Mot à trouver {} (encore {} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees:
            print("Vous avez déja chosi cette lettre.")
        elif lettre in mot_a_trouver:
            lettres_trouvees.append(lettre)
            print("Bien joué !")

        else:
            nb_chances -=1
            print(" ... non, cette lettre ne se trouve pas dans le mot ...")

        mot_trouve =recup_mot_masque(mot_a_trouver, lettres_trouvees)


    if mot_a_trouver == mot_trouve:
        print("Félicitation ! Vous avez trouvé le mot {}".format(mot_a_trouver))
    else:
        print("PENDU !!! Hhhhhhh vous avez perdu.")

    scores[utilisateur] += nb_chances
    continuer_partie = input("Souhaitez-vous quitter (o/n) ? : ")
    continuer_partie = continuer_partie.lower()

enregistrer_scores(scores)

print("Vous finiseez la partie avec {} point ".format(scores[utilisateur]))    
            
    
