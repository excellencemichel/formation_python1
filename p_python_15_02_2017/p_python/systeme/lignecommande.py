#Exemple de programme permetant de gérer la ligne de commande avec du code python

from sys import argv, exit #Module permetant d'intéragir avec le OS
         #'argv est une variable de 'sy' qui permet de capter les argume de la
         #ligne de commande

import argparse #Module pour interpreter la ligne de commande

if len(argv)<2: #si les argument de la ligne de commande sont < à 2
    print("Précisez une action en paramètre")
    exit(1)

action = argv[1] #le 1er argument reçcu par la variable

if action=="start":
    print("On démarre l'opération")
elif action=="stop":
    print("On arrête l'opération")
elif action =="restart":
    print("On redémarre l'opération")
elif action=="status":
    print("On affiche l'état (démarré ou arrêté ?) de l'opération")
else:
    print("Je ne connais pas cette action")


#________________________
#Utilisation du module argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="le nombre à mettre au carré")
parser.add_argument("-v", "--verbose", action="store_true", help ="augmente la verbosité")
args=parser.parse_args()

x= args.x
retour = x**2

if args.verbose:
    print("{} ^2 = {}".format(x,retour))
else:
    print(retour)


