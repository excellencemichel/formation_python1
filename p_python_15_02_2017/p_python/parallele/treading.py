#La programmation parallele

from threading import Thread, RLock  #Module pour la programmation parallèle
                             #RLock pour vérouiller une ressource partagée

"""
Dans un programme ordinaire de python, le code s'exécute de façon verticale, sur
un seul flux, ou bien les instructions s'exécute l'une après l'autre


Avec la programmation parallèle on peut palier cela en faisant exécuter plusieurs
parties du code en même temps avec l'outil 'threading'


Pour construire un code qui doit s'exécuter en threading on construis une classe
héritant de 'threading.Thread' et on modifi son contructeur et sa methode 'run'
 cette méthode 'run' doit contenir le code qui va s'exécuter en parallèle du
 reste du programme , cette étape s'appelle la définition des 'thread'
Après on les créé





"""
#Dabord pour un programme vertical
import time
print("Avant sleep ...")

time.sleep(1) #Met le programme en pose pendant (x) seconde (ici s)
print("Après sleep ...") #Ce message s'affiche après 3s de repos car le prog est
                         #de façcon verticale il que la fn sleep finisse



#________________________
#Un autre programme linéaire

import random
import sys
import time


#Répète 20 fois

i=0
while i<20:
    sys.stdout.write("1")
    sys.stdout.flush()#Dit à stdout d'afficher à l'immd le msg n ps attd la fin de l'exécution du code
    #print("1")
    attente = 0.2
    attente += random.randint(1,60)/1000000000000
    time.sleep(attente)
    i +=1



#Construction d'un programme en threading
print("Ecart")

verou = RLock()
class Afficher(Thread):

    """ Thread chargé d'afficher de la lettre  dans la console."""

    def __init__(self, lettre):
        """ Constructeur de la class Thread qu'on tente de redéfinir."""

        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """ Methode 'run' de la classe 'Thread' qui permet au code qui la
          de s'exécuter en parallèle



        """
        print("Michel")
        print("Marc")
        n = 0
        while n<10:
            with verou:
                
                for let in self.lettre:
                    
                
                    sys.stdout.write(let)
                    sys.stdout.flush() #Dit à sys.stdout.write d'afficher à l'immediat
                               #le msg ne pas attdre la fin de l'exé du prog
                    attend = 0.2
                    attend +=random.randint(1,60)/100
                    time.sleep(attend)
            n +=1

#Création des threads
thread_1 = Afficher("canard")
thread_2 = Afficher("TORTURE")
thread_3 = Afficher("trois")
thread_4 = Afficher("quatre")
thread_5 = Afficher("cinq")
thread_6 = Afficher("six")

#Lancement des threads
thread_1.start()
thread_2.start()
##thread_3.start()
##thread_4.start()
##thread_5.start()
##thread_6.start()
#Attend les threads se terminent, cela permet le code du thread termine normalem
thread_1.join()
thread_2.join()
##thread_3.join()
##thread_4.join()
##thread_5.join()
print("\n")
print("Barre")

class S:
    def __init__(self):
        self.nom="Michel"
        self.anom="Marc"

    def a(self):
        print(self.nom)
        print(self.anom)


ap=S()
ap1=S()
ap.a(), ap1.a()


