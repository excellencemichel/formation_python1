#Programmation système
import sys
import os
"""
Pyrthon est un language de programmation système,

Voici quelque module servant à intéragir avec le systhème d'exploitation
'sys' : Module servant le controle des flux standards

  -les flux standard de pythons sont :
     -entrée standard:  'stdin' : elle est appelée quand on utilise 'input'
     elle est donc utiliser pour pour recupérer les information des utilisateur.
        Par défaut l'entrée standard passe par le clavier

    -sorie standard: 'stdout'   : Elle est utilisée pour afficher les message. Par défaut
      les messages s'affiche à l'écran dont l'ecran est la sortie standard par
      défaut.

    -erreur standard:  'stderr'  : utiliser quand python veux afficherl'erreur
    (le traceback d'une exception.) par défaut elle est redirigée vers l'ecran,
    c-a-d la sortie standr des erreur par défaut c'est l'écran.


 Cest objet du module 'sys' sont de la même classe que la fonction 'open'
 ils ont donc les méthodes :
   read(): pour lire propre à 'stdin'

   write() : pour écire des messages


On peut donc changer la sortie ou l'entrée standard des ces objets vers d'autre
lieu comme dans des fichiers en changeant leur valeur


Après un changement de redirection, pour retablir les objet par défaut :
  entrée par défaut (clavier): __stdin__
  sortie par défaut (écran) : __stdout__
  sortie d'erreur par défaut (écran) : __stderr__


Seulement la redirection dans fichier pour y écrire des message, les méssage
ne s'écrivent pas dans le fichier malgré que les fichier se cré, cela n'est
d'abord possible avec l'éditeur IDLE

Mais avec l'invide de commande de python cela marche bien
  
 



"""


#Ridirection des flux
#Redirection de l'affichage des messages
fichier =open("sotiemessage.txt", "w") #On ouvre un fichier
sys.stdout = fichier #Au lieu que la sortie des messages soit sur l'écran on
                    #on la renvoi dans le fichier 'sortiemessage.txt' stocké
                   #dns la variable 'fichier'

print("Tu sort où ?")

sys.stdout= sys.__stdout__
print("Aff")

sortieerreur = open("sortieerreur.txt", "w")

sys.stderr = sortieerreur
print(variable,qui,exite,pas,leve,erreur,qui,sera,ecrit,dans,le,fichier,sortieerreur)




