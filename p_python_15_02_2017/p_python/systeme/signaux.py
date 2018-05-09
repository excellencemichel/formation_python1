#Les signaux
import sys
"""
Les signaux sont des moyens de faire communiquer le programme avec le système
d'exploitation

le module chargé de gérer les signaux s'appelle 'signal'
  Ce module contient beaucoup de signaux adaptés à chaque évenement, et quelque
  fois certains signaux diffèrent en fonction de os (système d'exploitation)

L'utilité des signaux est qu'on peut effectuer des opérations quand ces signaux
arrivent

    -le signale ' SIGINT' envoyé quand le programme doit s'arreter

"""

import signal #Module qui gère les signaux


print(signal.SIGINT)

#Soit une fonction doit s'exécuter quand le signal 'SIGINT' est envoyer
#Cette fonction prend deux parametre le signal (un ou plusieurs signaux) et le frame

def fermer_programme(signal, frame):
    """Fonction qui sera appelée quand vient l'heure de fermer le programme
     Pour que cette fonction soit appelé quand le signal est envoyé on doit
     conncter la fonction au signal

"""
    print("C'est l'heure de fermer le programme , fermer tout d'ailleurs")
    sys.exit(0) #Code envoyer pour fermer le programme, sinon le programme ne
               #va pas se fermer

#Connection de la fonction au signal
#Pour connecter un une fonction à un signal on  utilise la fonction 'signal' du
#module 'signal'

signal.signal(signal.SIGINT, fermer_programme) #Ce la permet de connecter 
          #la fonction au signal


print("On y va")
n=0
while n<10:
    print("Ca tourne jusqu'à hannnnnnnnnnn ...")
    n+=1

while True:
    continue #Ce la permet d'arrêter le progrmme car True est toujours vrai
             #quand tape ctrl + C pour arrêter le programme la fonction conncter
             #au signal sera appeler



    


